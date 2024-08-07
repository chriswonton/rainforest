#TODO - put login, sign up, basket, order, etc.

from repositories.account_repository import AccountRepository
from util.password_helper import encrypt_password

class UserService:
    def __init__(self):
        self.account_repo = AccountRepository()

    def validate_login(self, username, password):
        account = self.account_repo.select_account_username(username)
        if account is None:
            account = self.account_repo.select_account_email(username)
            if account is None:
                return None, "Account not found"

        if encrypt_password(password) != account[2]:
            return None, "Invalid password"

        return account, None

    def validate_signup(self, username, email, password, password2):
        accounts = self.account_repo.select_all_accounts()

        for account in accounts:
            if username == account[1]:
                return "Username already exists"
            if email == account[3]:
                return "Email already taken"

        if password != password2:
            return "Password 1 does not match Password 2"

        encrypted_password = encrypt_password(password)
        self.account_repo.insert_account(username, encrypted_password, email)
        return None
