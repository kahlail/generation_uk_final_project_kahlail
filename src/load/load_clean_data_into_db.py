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

def load_data_into_database(list_of_dicts: list, connection, cursor, key) -> True or False:
    i = 0
    print(f'load_data_into_database started, key = {key}')
    try:
        for dict in list_of_dicts:
            location = dict['Location']
            location_id = return_id('location_id', 'location', 'location_name', location, cursor)

            if location_id == None:
                location_sql = 'INSERT INTO location(location_name) VALUES (%s)'
                cursor.execute(location_sql, (dict['Location'],))
                location_id = return_id('location_id', 'location', 'location_name', dict['Location'], cursor)
            print(f'load_data_into_database {dict["Location"]} record added to location successfully')
        
            customer_name = dict['Name']
            customer_sql = 'INSERT INTO customers(customer_name) VALUES (%s)'
            cursor.execute(customer_sql, (customer_name,))
            customer_id = return_id('customer_id', 'customers', 'customer_name', customer_name, cursor)
            print(f'load_data_into_database customer_id = {customer_id} record added to customers successfully')

            transaction_values = (dict['Date Time'], customer_id, dict['Payment Method'], dict['Total'], location_id)
            transaction_sql = 'INSERT INTO customer_transactions(order_date, customer_id, payment_method, total_amount, location_id) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(transaction_sql, transaction_values)
            transaction_id = return_id('transaction_id', 'customer_transactions', 'customer_id', customer_id, cursor)
            print(f'load_data_into_database customer_id = {customer_id} record added to customer_transactions successfully')
            
            for string in dict['Order']:
                _ = 0
                order_values = (transaction_id, string)
                order_sql = 'INSERT INTO transaction_items(transaction_id, order_items) VALUES (%s, %s);'
                cursor.execute(order_sql, order_values)
                _ += 1
            print(f'load_data_into_database customer_id = {customer_id}, {_} record/s added to transaction_items table successfully')

            connection.commit()
            
            i += 1
        print(f'load_data_into_database successfully completed, key = {key} number of rows = {i}')
        return True, i
    except Exception as e:
        print(f'load_data_into_database failed to complete key = {key} line = {i + 1}: {e}')
        return False, i

    