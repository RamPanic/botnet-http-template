# General

IP_SERVER = "127.0.0.1"
PORT_SERVER = 5000

SECRET_KEY = "test"

# Database

MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "botnet"
MYSQL_PORT = 3306

DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{IP_SERVER}/{MYSQL_DATABASE}"

# Debugging

DEBUG = True