
from db_connection import get_connection

def insert_account(username, password, email):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Account (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, email))
        connection.commit()
    finally:
        connection.close()

def insert_product(name, manufacturer, description, price, stock):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Product (name, manufacturer, description, price, inventory_stock) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, manufacturer, description, price, stock))
        connection.commit()
    finally:
        connection.close()

def insert_order(account_id, total):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Order (account_id, product_id, order_date, total) VALUES (%s, %s)"
            cursor.execute(sql, (account_id, total))
            order_id = cursor.lastrowid
        connection.commit()
        return order_id
    finally:
        connection.close()

# def insert_order_product(order_id, product_id, quantity):
#     connection = get_connection()
#     try:
#         with connection.cursor() as cursor:
#             sql = "INSERT INTO order_product (order_id, product_id, quantity) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (order_id, product_id, quantity))
#         connection.commit()
#     finally:
#         connection.close()

# def insert_shipment(order_id, delivery_date, status):
#     connection = get_connection()
#     try:
#         with connection.cursor() as cursor:
#             sql = "INSERT INTO shipment (order_id, delivery_date, status) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (order_id, delivery_date, status))
#         connection.commit()
#     finally:
#         connection.close()

def select_account(username):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Account WHERE username = %s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            return result
    finally:
        connection.close()