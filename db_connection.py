import os
from dotenv import load_dotenv
import pymysql

# Load environment variables from .env file
load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

# if __name__ == '__main__':
#     try:
#         connection = get_connection()
#         print("Connection to the database was successful!")
#         connection.close()
#     except Exception as e:
#         print(f"An error occurred: {e}")