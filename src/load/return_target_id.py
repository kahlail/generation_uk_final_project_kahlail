def return_id(id_column_name, table_name, value_reference, target_value, cursor):
    try:    
        sql = f"SELECT {id_column_name} FROM {table_name} WHERE {value_reference} = '{target_value}'"
        cursor.execute(sql)
        target_id = cursor.fetchone()[0]
        if target_id:
            return target_id
        return None    
    
    except Exception as e:
        print(f'retrieving target id ({target_value}) failed  - id column name = {id_column_name}, table name = {table_name}: {e}')  