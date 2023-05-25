import os
import psycopg2 as psy
from dotenv import load_dotenv

load_dotenv("../utils/.env")
HOST = os.environ.get("postgres_host")
USER = os.environ.get("postgres_user")
PASSWORD = os.environ.get("postgres_pass")
DB_NAME = os.environ.get("postgres_db")

db_connection = None

def open_sql_database_connection_and_cursor() -> db_connection and db_connection.cursor():
    try:    
        global db_connection
        if db_connection:
            print('Connection already running.')
        else:
            print('New connection starting...')
            db_connection = psy.connect(host=HOST, database=DB_NAME,
                                             user=USER, password=PASSWORD)
        cursor = db_connection.cursor()
        return db_connection, cursor
    except ConnectionError as e:
        print(f'Failed to open connection:\n{e}')