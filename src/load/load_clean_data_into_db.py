def load_data_into_database(list_of_dicts: list, connection, cursor, key, return_id_func) -> True or False:
    i = 0
    print(f'load_data_into_database started, key = {key}')
    try:
        for data in list_of_dicts:
            location = data['Location']
            location_id = return_id_func('location_id', 'location', 'location_name', location, cursor)

            if location_id == None:
                location_sql = 'INSERT INTO location(location_name) VALUES (%s)'
                cursor.execute(location_sql, (data['Location'],))
                location_id = return_id_func('location_id', 'location', 'location_name', data['Location'], cursor)
            print(f'load_data_into_database {data["Location"]} record added to location successfully')
        
            customer_name = data['Name']
            customer_sql = 'INSERT INTO customers(customer_name) VALUES (%s)'
            cursor.execute(customer_sql, (customer_name,))
            customer_id = return_id_func('customer_id', 'customers', 'customer_name', customer_name, cursor)
            print(f'load_data_into_database customer_id = {customer_id} record added to customers successfully')

            transaction_values = (data['Date Time'], customer_id, data['Payment Method'], data['Total'], location_id)
            transaction_sql = 'INSERT INTO customer_transactions(order_date, customer_id, payment_method, total_amount, location_id) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(transaction_sql, transaction_values)
            transaction_id = return_id_func('transaction_id', 'customer_transactions', 'customer_id', customer_id, cursor)
            print(f'load_data_into_database customer_id = {customer_id} record added to customer_transactions successfully')
            
            _ = 0
            order_values_list = []
            for order_string, order_price in zip(data['Order'], data['Order Price']):
                order_values = (transaction_id, order_string, order_price)
                order_values_list.append(order_values)
                _ += 1
            order_sql = 'INSERT INTO transaction_items(transaction_id, order_items, order_price) VALUES (%s, %s, %s);'
            cursor.executemany(order_sql, order_values_list)
            print(f'load_data_into_database customer_id = {customer_id}, {_} record/s added to transaction_items table successfully')

            connection.commit()
            
            i += 1
        print(f'load_data_into_database successfully completed, key = {key} number of rows = {i}')
        return True, i
    
    except Exception as e:
        print(f'load_data_into_database failed to complete key = {key} row = {i + 1}: {e}')
        return False, i