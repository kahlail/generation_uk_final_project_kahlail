from local_app.generate_sql_db import create_db_tables
from unittest.mock import Mock


def test_create_db_tables():
    mock_connection = Mock()
    mock_cursor = Mock()

    expected_result = True
    actual_result = create_db_tables(mock_connection, mock_cursor)

    assert expected_result == actual_result
    assert mock_cursor.execute.call_count == 4
    assert mock_connection.commit.call_count == 1
    