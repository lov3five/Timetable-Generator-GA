import os
import mysql_helper
from mysql_helper import connect_to_mysql
from dotenv import load_dotenv
load_dotenv()

# Info MySQL Server
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connect to MySQL database
mydb = connect_to_mysql(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

