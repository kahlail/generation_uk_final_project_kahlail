from unittest.mock import Mock
from src.load.load_clean_data_into_db import return_id

def test_return_id():
    mock_cursor = Mock()
    mock_cursor.fetchone = Mock(return_value=[99])

    actual_result = return_id('mock_id', 'mock_table', 'mock_column_value', 'mock_value', mock_cursor)
    expected_result = 99

    assert mock_cursor.execute.call_count == 1
    assert actual_result == expected_result
    mock_cursor.execute.assert_called_once_with("SELECT mock_id FROM mock_table WHERE mock_column_value = 'mock_value'")
    