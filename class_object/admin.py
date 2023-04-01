class Admin():
    def __init__(self, username:str, password:str, first_name:str, last_name:str, email:str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._username = username
        self._password = password 
