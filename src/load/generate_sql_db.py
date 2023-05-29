def create_db_tables(connection, cursor) -> True or False:
    print('create_db_tables started')
    try: 
        print('...creating location')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS location (
            location_id INT IDENTITY(1, 1) PRIMARY KEY,
            location_name VARCHAR(250) NOT NULL UNIQUE
        );
        """)
        
        print('...creating customers')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT IDENTITY(1, 1) PRIMARY KEY,
            customer_name VARCHAR(250) NOT NULL
        );
        """)
        
        print('...creating customer_transactions')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_transactions (
            transaction_id INT IDENTITY(1, 1) PRIMARY KEY,
            order_date TIMESTAMP NOT NULL,
            customer_id INT NOT NULL,
            payment_method VARCHAR(10) NOT NULL,
            total_amount DECIMAL(6,2) NOT NULL,
            location_id INT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (location_id) REFERENCES location(location_id)
        );
        """)
        
        print('...creating transaction_items')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaction_items (
            transaction_items_id INT IDENTITY(1, 1) PRIMARY KEY,
            transaction_id INT NOT NULL,
            order_items VARCHAR(250)
        );
        """)
        connection.commit()
        print('...committed')
        print('create_db_tables successfull')
        return True
    
    except Exception as ex:
        print(f'create_db_tables failed to generate table/s:\n{ex}')
        return False
        
