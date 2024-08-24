#TODO - add database access - Inject database connection to this class
from util.connection_helper import get_connection
class AdminRepository:
    def __init__(self, connection=None):
        self.connection = connection or get_connection()

    def insert_product(self, name, manufacturer, description, image, category, price, stock):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO Product (name, manufacturer, description, image, category, price, inventory_stock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, manufacturer, description, image, category, price, stock))
        self.connection.commit()

    def select_all_users(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Account LIMIT 100"
            cursor.execute(sql)
            results = cursor.fetchall()
            self.connection.commit()
            return results
        
    def update_user(self, username, email, is_admin, is_active):
        with self.connection.cursor() as cursor:
            sql = """
                UPDATE Account
                SET email = %s, admin = %s, activity = %s
                WHERE username = %s
            """
            cursor.execute(sql, (email, is_admin, is_active, username))
        self.connection.commit()