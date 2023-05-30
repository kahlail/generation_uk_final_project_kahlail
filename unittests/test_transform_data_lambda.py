from src.transform.transform_data_lambda import transform_raw_data
from src.transform.format_date_lambda import format_date_time

def test_transformed_data():
    # Arrange
    test_data = [{'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': 'Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45', 'Total': 5.2, 'Payment Method': 'CARD'}]
    expected_output = [{'Date Time': '2021-08-25 09:00:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': ['Regular Flavoured iced latte - Hazelnut', 'Large Latte'], 'Order Price': ['2.75', '2.45'], 'Total': 5.2, 'Payment Method': 'CARD'}]
    mock_key = 'test_key'

    # Act
    result = transform_raw_data(test_data, mock_key, format_date_time)

    # Assert
    assert result == expected_output