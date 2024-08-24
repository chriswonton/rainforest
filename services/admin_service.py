#TODO - put admin function such as manage users, edit users, manage product

from repositories.admin_repository import AdminRepository
from datetime import datetime

class AdminService:
    # self.adminRepo = AdminRepository()
    def __init__(self):
        self.admin_repo = AdminRepository()
    
    # get_user_list(self):
        # user_list_df = self.adminRepo.get_user_list()
        # Validate user_list/filter out inactive user, create compute field: first name + last name
        # to show the full username and add the new field to the dataframe
        # compute the age on the fly 

    def get_user_list(self):
        user_list = self.admin_repo.get_user_list()
        
        active_users = [user for user in user_list if user['active']]

        # Add a full name field
        # for user in active_users:
        #     user['full_name'] = f"{user['first_name']} {user['last_name']}"

        #     # Calculate the user's age based on their birthdate
        #     birthdate = user['birthdate']  # Assuming birthdate is a date object
        #     age = (datetime.now().date() - birthdate).days // 365
        #     user['age'] = age

        return active_users

    def insert_product(self, name, manufacturer, description, image, category, price, stock):
        self.admin_repo.insert_product(name, manufacturer, description, image, category, price, stock)

    def get_all_users(self):
        return self.admin_repo.select_all_users()
    
    def update_user(self, username, email, is_admin, is_active):
        is_admin_int = 1 if is_admin else 0
        is_active_int = 1 if is_active else 0

        self.admin_repo.update_user(username, email, is_admin_int, is_active_int)