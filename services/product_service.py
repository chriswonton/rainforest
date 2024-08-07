#TODO - add product specific funtinon like adding new product, manage inventory, etc.

from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()

    def get_all_products(self):
        return self.product_repo.select_all_products()

    def get_product_by_id(self, product_id):
        return self.product_repo.select_product_id(product_id)

    def add_order(self, username, product_id, quantity):
        account = self.product_repo.select_account_username(username)
        if not account:
            return None, "User not found"
        
        account_id = account[0]
        order_id = self.product_repo.select_order_cart(account_id)
        if order_id is None:
            order_id = self.product_repo.insert_order(account_id)
        
        self.product_repo.insert_order_item(order_id, product_id, quantity)
        return "Product added to shopping cart", None

    def get_shopping_cart(self, username):
        account = self.product_repo.select_account_username(username)
        if not account:
            return None, "User not found"
        
        account_id = account[0]
        order_id = self.product_repo.select_order_cart(account_id)
        if order_id is None:
            order_id = self.product_repo.insert_order(account_id)
        
        order_items = self.product_repo.select_order_item_id(order_id)
        total_price = sum(product[5] * product[2] for product in order_items)
        
        return order_items, total_price, None

    def buy_items(self, username):
        account = self.product_repo.select_account_username(username)
        if not account:
            return None, "User not found"
        
        account_id = account[0]
        order_id = self.product_repo.select_order_cart(account_id)
        if order_id is None:
            order_id = self.product_repo.insert_order(account_id)
        
        self.product_repo.update_product_stock(order_id)
        self.product_repo.update_order_date(order_id)
        
        return "Bought items", None
