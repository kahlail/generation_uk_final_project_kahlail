from local_app.load_clean_data_into_db import load_data_into_database
from unittest.mock import Mock


def test_load_data_into_db():
    mock_connection = Mock()
    mock_cursor = Mock()
    mock_data = [
        {'Date Time': '21/08/2021 09:00', 'Location': 'London', 'Name': 'Sally Hugh', 'Order': ['Regular Flavoured iced latte - Hazelnut - 2.75'], 'Total': '7.1','Payment Method': 'CASH'},
        {'Date Time': '23/08/2021 18:30', 'Location': 'Chesterfeild', 'Name': 'Jane Doe', 'Order': ['Regular latte - Vanilla - 2.75'], 'Total': '3.5','Payment Method': 'CARD'},
        {'Date Time': '25/08/2021 16:00', 'Location': 'Liverpool', 'Name': 'Joe Bloggs', 'Order': ['Large Flavoured iced latte - Hazelnut - 2.75', 'Flat white - 2.10' ], 'Total': '12.1','Payment Method': 'CARD'},
        {'Date Time': '29/08/2021 07:00', 'Location': 'London', 'Name': 'Dennis Menace', 'Order': ['Regular Flavoured iced latte - Hazelnut - 2.75'], 'Total': '17.5','Payment Method': 'CARD'},
        {'Date Time': '29/08/2021 12:00', 'Location': 'Manchester', 'Name': 'Emma Walker', 'Order': ['Large Flavoured iced latte - Caramel - 2.75', 'Regular Latte - 3.10', 'Flat white - £2.12'], 'Total': '9.9','Payment Method': 'CASH'}
    ]

    expected_result = True
    actual_result = load_data_into_database(mock_data, mock_cursor, mock_connection)

    assert expected_result == actual_result
    assert mock_cursor.execute.call_count == 23
    assert mock_connection.commit.call_count == 5