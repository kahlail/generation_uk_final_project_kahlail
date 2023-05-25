from src.transform.format_date_lambda import format_date_time

def test_format_date_time():

    input_data = [
        {'Date Time': '02/02/2022 14:00'},
        {'Date Time': '04/04/2044 16:40'}
    ]

    expected_data = [
        {'Date Time': '2022-02-02 14:00:00'},
        {'Date Time': '2044-04-04 16:40:00'}        
    ]

    output = format_date_time(input_data)

    assert output == expected_data

    for dict in output:
        assert isinstance(dict['Date Time'], str)


