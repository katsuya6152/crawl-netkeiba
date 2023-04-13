from dotenv import load_dotenv
load_dotenv(dotenv_path='../mysql/.env')

import os

# If you are in a local environment, use this one
# DB_USER = os.getenv('DB_USER')
# PASSWORD = os.getenv('DB_PASS')
# HOST = os.getenv('LOCAL_HOST')
# DATABASE = os.getenv('DB_NAME')

DB_USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')