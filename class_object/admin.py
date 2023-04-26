from user import User

class Admin(User):
    def __init__(self, username:str, hashed_password:str, first_name:str, last_name:str, email:str) -> None:
        User.__init__(self, username, hashed_password, first_name, last_name, email)
