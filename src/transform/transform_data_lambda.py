def transform_raw_data(data, key, format_date_func):
    i = 0
    print(f'transform_raw_data started, key = {key}')
    
    con_data = format_date_func(data)
    
    try:
        transformed_list = []

        for row in con_data:
            orders = []

            order_name = row['Order'].split(',')
            
            orders = [it[0:-6].strip() for it in order_name]
            order_price = [i.rsplit(' - ', 1)[-1] for i in order_name]
        
            transformed_list.append({'Date Time': row['Date Time'], 'Location': row['Location'], 'Name': row['Name'], 'Order': orders, 'Order Price': order_price, 'Total': row['Total'],'Payment Method': row['Payment Method']})

            i += 1
        print(f'transform_raw_data successfully transformed data, key = {key} number of rows = {i}')
        return transformed_list
    
    except Exception as e:
        print(f'transform_raw_data failed row = {i + 1} key = {key}: {e}')