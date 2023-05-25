from datetime import datetime

def format_date_time(list_of_dicts):
    try:
        for dict in list_of_dicts:
            date_value = datetime.strptime(dict['Date Time'], '%d/%m/%Y %H:%M')
            date_value = datetime.strftime(date_value, '%Y-%m-%d %H:%M:%S')
            dict['Date Time'] = date_value
        print('format_date_time successfully coverted date strings')    
        return list_of_dicts
    
    except Exception as e:
        print(f'format_date_time failed to convert date string: {e}')