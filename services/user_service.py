#TODO - put login, sign up, basket, order, etc.

from repositories.user_repository import UserRepository
from util.password_helper import encrypt_password

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def validate_login(self, username, password):
        account = self.user_repo.select_account_username(username)
        if account is None:
            account = self.user_repo.select_account_email(username)
            if account is None:
                return None, "Invalid username"

        if encrypt_password(password) != account[2]:
            return None, "Invalid password"
        
        self.user_repo.update_last_login(username)
        return account, None

    def validate_signup(self, username, email, password, password2):
        accounts = self.user_repo.select_all_accounts()

        for account in accounts:
            if username == account[1]:
                return "Username already exists"
            if email == account[3]:
                return "Email already taken"

        if password != password2:
            return "Password 1 does not match Password 2"

        encrypted_password = encrypt_password(password)
        self.user_repo.insert_account(username, encrypted_password, email)
        return None