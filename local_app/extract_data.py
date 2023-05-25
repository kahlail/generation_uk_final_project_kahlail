import csv
def  read_brew_csv(file_path):
    try:
        
        with open(file_path, 'r') as file:
            new_data = []
            reader = csv.reader(file)
            for row in reader:
                new_data.append({'Date Time': row[0], 'Location': row[1], 'Name': row[2], 'Order': row[3], 'Total': row[4],'Payment Method': row[5], 'Card No': row[6]})
        
        return new_data
    
    except Exception as e:
        print(f'Error, file not read: {e}')
