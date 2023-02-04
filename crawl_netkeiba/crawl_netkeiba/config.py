from dotenv import load_dotenv
load_dotenv()

import os

DB_USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASS')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DB_NAME')