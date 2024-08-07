#TODO - add database access - Inject database connection to this class
from util.connection_helper import get_connection

class AdminRepository:
    # self.connection = inject connection object
    def __init__(self):
        pass
        
    def insert_product(self, name, manufacturer, description, image, category, price, stock):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Product (name, manufacturer, description, image, category, price, inventory_stock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (name, manufacturer, description, image, category, price, stock))
            connection.commit()
        finally:
            connection.close()