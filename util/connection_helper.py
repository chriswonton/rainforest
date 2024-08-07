#TODO - put connection creation here 

import os
from dotenv import load_dotenv
import pymysql

# Load environment variables from .env file
load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),  # TODO - Store this in secret manager on AWS
        database=os.getenv('DB_NAME')       #Store this in secret manager on AWS
    )