from connect_to_db import *
from generate_sql_db import *
from load_clean_data_into_db import *
from transform_data import *
from extract_data import *

if __name__ == "__main__":
    print('Local ETL programme running')
    
    # TO DO: Add correct file path below
    file_path = ''
    
    # extract_function()
    list_of_dicts = read_brew_csv(file_path)
    print('Data successfully extracted')

    # transform
    transformed_data = transform_data(list_of_dicts)
    print('Data successfully transformed')

    # load
    conn, cur = open_sql_database_connection_and_cursor
    create_db_tables(conn, cur)
    load_data_into_database(transformed_data, conn, cur)
    print('Data successfully loaded.\nApplication finished.')