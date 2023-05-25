from format_date_lambda import format_date_time

def transform_raw_data(data, key):
    i = 0
    print(f'transform_raw_data started, key = {key}')
    
    con_data = format_date_time(data)
    
    try:
        transformed_list = []

        for row in con_data:
            orders = []

            order_name = row['Order'].split(',')
            for order in order_name:
                orders.append(order.strip())
            
            transformed_list.append({'Date Time': row['Date Time'], 'Location': row['Location'], 'Name': row['Name'], 'Order': orders , 'Total': row['Total'],'Payment Method': row['Payment Method']})
            
            i += 1
        print(f'transform_raw_data successfully transformed data, key = {key} number of rows = {i}')
        return transformed_list
    
    except Exception as e:
        print(f'transform_raw_data failed row = {i + 1} key = {key}: {e}')
        











