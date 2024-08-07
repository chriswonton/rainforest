from util.connection_helper import get_connection

class ProductRepository:
    def __init__(self):
        pass

    def select_product_id(self, product_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Product WHERE product_id = %s"
                cursor.execute(sql, (product_id))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()

    def select_all_products(self):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Product"
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
        finally:
            connection.close()

    def insert_order(self, account_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `Order` (account_id) VALUE (%s)"
                cursor.execute(sql, (account_id))
            connection.commit()
            order_id = cursor.lastrowid
            return order_id
        finally:
            connection.close()

    def select_order_cart(self, account_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT order_id FROM `Order` WHERE account_id = %s AND order_date IS NULL"
                cursor.execute(sql, (account_id))
                result = cursor.fetchone()
                if result:
                    return result[0]
                return None
        finally:
            connection.close()

    def insert_order_item(self, order_id, product_id, quantity):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Order_Item (order_id, product_id, quantity) VALUES (%s, %s, %s)"
                cursor.execute(sql, (order_id, product_id, quantity))
            connection.commit()
        finally:
            connection.close()

    def select_order_item_id(self, order_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT 
                        Order_Item.order_id,
                        Order_Item.product_id,
                        Order_Item.quantity,
                        Product.name,
                        Product.image,
                        Product.price
                    FROM 
                        Order_Item
                    INNER JOIN 
                        Product ON Order_Item.product_id = Product.product_id
                    WHERE 
                        Order_Item.order_id = %s
                """
                cursor.execute(sql, (order_id,))
                results = cursor.fetchall()
                return results
        finally:
            connection.close()

    def update_product_stock(self, order_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE Product AS p
                    JOIN Order_Item AS oi ON p.product_id = oi.product_id
                    SET p.inventory_stock = p.inventory_stock - oi.quantity
                    WHERE oi.order_id = %s
                """
                cursor.execute(sql, (order_id,))
                connection.commit()
        finally:
            connection.close()

    def update_order_date(self, order_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE `Order` SET order_date = CURRENT_DATE WHERE order_id = %s"
                cursor.execute(sql, (order_id,))
                connection.commit()
        finally:
            connection.close()

    def select_account_username(self, username):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Account WHERE username = %s"
                cursor.execute(sql, (username))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()