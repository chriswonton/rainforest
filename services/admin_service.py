#TODO - put admin function such as manage users, edit users, manage product

from repositories.admin_repository import AdminRepository

class AdminService:
    # self.adminRepo = AdminRepository()
    def __init__(self):
        self.admin_repo = AdminRepository

    # get_user_list(self):
        # user_list_df = self.adminRepo.get_user_list()
        # Validate user_list/filter out inactive user, create compute field: first name + last name
        # to show the full username and add the new field to the dataframe
        # compute the age on the fly 

    def add_product(self, name, manufacturer, description, image, category, price, stock):
        self.admin_repo.insert_product(name, manufacturer, description, image, category, price, stock)