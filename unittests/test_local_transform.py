from local_app.transform_data import transform_data

def test_transformed_data():
    # Arrange
    data = [{'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': 'Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45', 'Total': 5.2, 'Payment Method': 'CARD'},]
            
    expected_output = [{'Date Time': '25/08/2021 09:00', 'Location': 'Chesterfield', 'Name': 'LBOwNxrHEd', 'Order': ['Regular Flavoured iced latte - Hazelnut - 2.75', 'Large Latte - 2.45'], 'Total': 5.2, 'Payment Method': 'CARD'},]
                       

    # Act
    result = transform_data(data)

    # Assert
    assert result == expected_output