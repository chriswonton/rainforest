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