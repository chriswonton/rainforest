from util.connection_helper import get_connection

class UserRepository:
    def __init__(self, connection=None):
        self.connection = connection or get_connection()

    def insert_account(self, username, password, email):
        with self.onnection.cursor() as cursor:
            sql = "INSERT INTO Account (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, email))
        self.connection.commit()

    def select_account_username(self, username):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Account WHERE username = %s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            return result

    def select_account_email(self, email):
        with self.connection.cursor() as cursor:    #TODO discrete field not ALL 
            sql = "SELECT * FROM Account WHERE email = %s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            return result

    def select_all_accounts(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Account"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
    
    def update_last_login(self, username):
        with self.connection.cursor() as cursor:
            sql = """
            UPDATE Account
            SET last_login = NOW(), activity = 1
            WHERE username = %s
            """
            cursor.execute(sql, (username,))
        self.connection.commit()