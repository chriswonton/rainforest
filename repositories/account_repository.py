from util.connection_helper import get_connection

class AccountRepository:
    def __init__(self):
        pass

    def insert_account(self, username, password, email):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Account (username, password, email) VALUES (%s, %s, %s)"
                cursor.execute(sql, (username, password, email))
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

    def select_account_email(self, email):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:  #TODO
                sql = "SELECT discret field not ALL * FROM Account WHERE email = %s"
                cursor.execute(sql, (email))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()

    def select_all_accounts(self):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Account"
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
        finally:
            connection.close()