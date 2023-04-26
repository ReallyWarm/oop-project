import sys
sys.path.append('./class_object/')
from auth import Authenticate
auth = Authenticate()
n = input('Password: ')
print(auth.get_password_hash(n))