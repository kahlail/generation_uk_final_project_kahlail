from connect_to_db import *

def load_data_into_database(list_of_dicts: list, cursor, connection) -> True or False:
    i = 0
    try:
        for dict in list_of_dicts:
            location = dict['Location']
            location_sql = 'SELECT location_id FROM location WHERE location_name LIKE %s'
            location_id = cursor.execute(location_sql, location)
            if location_id == None:
                new_location = dict['Location'].title()
                location_sql = 'INSERT INTO location(location_name) VALUES (%s) RETURNING location_id'
                location_id = cursor.execute(location_id, new_location)
        
            customer_value = dict['Name']
            customer_sql = 'INSERT INTO customers(customer_name) VALUES (%s) RETURNING customer_id'
            customer_id = cursor.execute(customer_sql, customer_value)
            
            transaction_values = (dict['Date Time'], customer_id, dict['Payment Method'], dict['Total'], location_id)
            transaction_sql = 'INSERT INTO customer_transactions(order_date, customer_id, payment_method, total_amount, location_id) VALUES (%s, %s, %s, %s, %s) RETURNING transaction_id'
            transaction_id = cursor.execute(transaction_sql, transaction_values)
            
            for string in dict['Order']:
                order_values = (transaction_id, string)
                order_sql = 'INSERT INTO transaction_items(transaction_id, order_items) VALUES (%s, %s);'
                cursor.execute(order_sql, order_values)
            connection.commit()
            i += 1
        return True
    
    except Exception as e:
        print(f'Data entry to databse failed to complete at line {i + 1}: {e}')
        return False

    