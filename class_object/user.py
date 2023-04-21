class User:
    def __init__(self, username:str, hashed_password:str, first_name:str, last_name:str, email:str) -> None:
        self._username = username
        self._hashed_password = hashed_password
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def username(self) -> str:
        return self._username
    
    @property
    def hashed_password(self) -> str:
        return self._hashed_password
    
    @property
    def first_name(self) -> str:
        return self._first_name