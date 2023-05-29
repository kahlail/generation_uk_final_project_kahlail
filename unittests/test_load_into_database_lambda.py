from src.load.load_clean_data_into_db import load_data_into_database
from unittest.mock import Mock

def test_load_data_into_database():
    mock_list_of_dicts = [
        {'Date Time': '2044-04-04 16:40:00', 
         'Location': 'London Covent Garden', 
         'Name': 'test_case_1', 
         'Order': ['order string 1'], 
         'Total': 2.5, 
         'Payment Method': 'CARD'},

        {'Date Time': '2044-04-04 16:40:00', 
         'Location': 'Chesterfield', 
         'Name': 'test_case_2', 
         'Order': ['order string 2', 'order string 3'], 
         'Total': 5.0, 
         'Payment Method': 'CARD'},

        {'Date Time': '2044-04-04 16:40:00', 
         'Location': 'Bristol', 
         'Name': 'test_case_3', 
         'Order': ['order string 4', 'order string 5', 'order string 6'], 
         'Total': 7.5, 
         'Payment Method': 'CARD'},
    ]

    mock_connection = Mock()
    mock_cursor = Mock()
    mock_key = 'mock_file.csv'
    mock_return_id_func = Mock()
    mock_return_id_func.side_effect = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    expected_result = True, 3
    actual_result = load_data_into_database(mock_list_of_dicts, mock_connection, mock_cursor, mock_key, mock_return_id_func)
    
    assert expected_result == actual_result
    assert mock_cursor.execute.call_count == 12
    assert mock_connection.commit.call_count == 3
    