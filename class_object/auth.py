import os
from fastapi import HTTPException, status
from jose import JWTError, jwt

from user import User

from datetime import datetime, timedelta
from passlib.context import CryptContext

class Authenticate():
    os.environ['API_TOKEN'] = ''
    __SECRET_KEY = "608672d916b11ac31e9ac553d5418caec4052bca348f2d06d4440aaacce155b0"
    __ALGORITHM = "HS256"
    __ACCESS_TOKEN_EXPIRE_MINUTES = 30
    __pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)
        
    def authenticate_user(self, user: User, password: str):
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expires_delta = timedelta(minutes=self.__ACCESS_TOKEN_EXPIRE_MINUTES)
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)
        os.environ['API_TOKEN'] = encoded_jwt
        return encoded_jwt

    def get_current_user(self):
        token: str = os.environ['API_TOKEN']
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You're not logged in")
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGORITHM])
            if payload is None:
                raise credentials_exception
            return { "user": payload['sub'], "exp": payload['exp'] }
        except JWTError:
            raise credentials_exception
        
    def invalidate_token(self):
        os.environ['API_TOKEN'] = ''