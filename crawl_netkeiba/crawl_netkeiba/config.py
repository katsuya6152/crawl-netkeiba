from dotenv import load_dotenv
load_dotenv(dotenv_path='../mysql/.env')

import os

DB_USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASS')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DB_NAME')