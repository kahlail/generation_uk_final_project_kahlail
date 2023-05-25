from local_app.extract_data import read_brew_csv

def test_extract_csv_correct_output(tmpdir):
    # Arrange
    # Create a temporary CSV file for testing
    file_path = tmpdir.join("test.csv")
    with open(file_path, 'w') as file:
        file.write("25/08/2021 09:00,Chesterfield,LBOwNxrHEd,\"Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45\",5.2,CARD,2978328181139200\n")
        
    # Call the function and check the output
    data = read_brew_csv(file_path)
    print(data)
  # Assert
    assert data == [
        {'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': "Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45", 'Total': '5.2', 'Payment Method': 'CARD', 'Card No':'2978328181139200'},
        
       ]