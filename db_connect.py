import pymysql

def get_connection():
    return pymysql.connect(
        host='your_rds_endpoint',
        user='your_db_username',
        password='your_db_password',
        database='your_db_name'
    )
