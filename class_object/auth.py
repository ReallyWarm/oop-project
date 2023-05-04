from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from customerinfo import CustomerInfo
    from admin import Admin

import os
from fastapi import HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

class Authenticate():
    os.environ['API_TOKEN'] = ''
    __secret_key:str = "608672d916b11ac31e9ac553d5418caec4052bca348f2d06d4440aaacce155b0"
    __algorithm:str = "HS256"
    __access_token_expire_minutes:int = 30
    __pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password:str, hashed_password:str) -> bool:
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password:str) -> str:
        return self.__pwd_context.hash(password)
        
    def authenticate_user(self, user: CustomerInfo|Admin, password: str) -> CustomerInfo| Admin | False:
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(self, user_data: dict) -> str:
        to_encode = user_data.copy()
        expires_delta = timedelta(minutes=self.__access_token_expire_minutes)
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.__secret_key, algorithm=self.__algorithm)
        os.environ['API_TOKEN'] = encoded_jwt
        return encoded_jwt

    def get_current_user(self) -> dict:
        token: str = os.environ['API_TOKEN']
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You're not logged in")
        try:
            payload = jwt.decode(token, self.__secret_key, algorithms=[self.__algorithm])
            if payload is None:
                raise credentials_exception
            return { "user": payload['sub'], "exp": payload['exp'] }
        except JWTError:
            raise credentials_exception
        
    def invalidate_token(self) -> None:
        os.environ['API_TOKEN'] = ''