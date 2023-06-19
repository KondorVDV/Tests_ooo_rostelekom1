import os
from dotenv import load_dotenv

load_dotenv()

user_email = os.getenv('user_email')
user_phone = os.getenv('user_phone')
user_personal_account = os.getenv('user_personal_account')
user_login = os.getenv('user_login')
password = os.getenv('password')