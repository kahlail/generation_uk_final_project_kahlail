import psycopg2 as psy
import boto3
import json

ssm_client = boto3.client('ssm')
parameter_details = ssm_client.get_parameter(Name='brew-tea-full-redshift-settings')
redshift_details = json.loads(parameter_details['Parameter']['Value'])

HOST = redshift_details['host']
USER = redshift_details['user']
PASSWORD = redshift_details['password']
DB_NAME = redshift_details['database-name']
PORT = redshift_details['port']

def open_sql_database_connection_and_cursor():
    try:    
        print('open_sql_database_connection_and_cursor - new connection starting...')
        db_connection = psy.connect(host=HOST, database=DB_NAME,
                                            user=USER, password=PASSWORD, port=PORT)
        cursor = db_connection.cursor()
        return db_connection, cursor
    
    except ConnectionError as e:
        print(f'open_sql_database_connection_and_cursor - failed to open connection:\n{e}')