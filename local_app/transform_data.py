def transform_data(data):

    try:
        transformed_list = []
        for row in data:
            orders = []
            order_name = row['Order'].split(',')
            for order in order_name:
                orders.append(order.strip())
            
            transformed_list.append({'Date Time': row['Date Time'], 'Location': row['Location'], 'Name': row['Name'], 'Order': orders , 'Total': row['Total'],'Payment Method': row['Payment Method']})

        return transformed_list
    except Exception as e:
        print(f'Not able to transform file: {e}')












