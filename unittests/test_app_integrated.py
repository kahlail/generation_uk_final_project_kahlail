from src.extract.extract_data_lambda import extract_csv
from src.transform.format_date_lambda import format_date_time
from src.transform.transform_data_lambda import transform_raw_data
from src.load.generate_sql_db import create_db_tables
from src.load.load_clean_data_into_db import return_id
from src.load.load_clean_data_into_db import load_data_into_database
from unittest.mock import Mock
from moto import mock_s3
import boto3
import os
import pytest

# Mock database connection objects
conn = Mock()
cur = Mock()

@pytest.fixture
def test_integrated_lambda_function():
    
    # Mock AWS bucket and key using moto and test credentials
    s3_client = boto3.client("s3", region_name='eu-west-1')
    bucket = s3_client.create_bucket(Bucket='test_bucket')
    key = 'test.csv'
    file_path = '/Users/User/Documents/CODING/GitHub_Profile/generation_uk_final_project_kahlail/unittests/test.csv'
    
    # Upload test.csv file to mock bucket
    s3_client.upload_file(file_path, bucket)

    # _________________________________ Replicate lambda_handler.lambda_function below_________________________________

    # extract mock test.csv
    expected_raw_data = [
        {'Date Time': row[0], 
         'Location': row[1], 
         'Name': row[2], 
         'Order': row[3], 
         'Total': row[4],
         'Payment Method': row[5], 
         'Card No': row[6]}
    ]

    raw_data = extract_csv(bucket, key)

    assert raw_data == list
    assert len(raw_data) == 20
    for row in raw_data:
        assert expected_raw_data == row

    # transform test.csv data
    expected_transformed_data = [
        {'Date Time': row[0], 
         'Location': row[1], 
         'Name': row[2], 
         'Order': row[3], 
         'Total': row[4],
         'Payment Method': row[5]}
    ]
    trans_data = transform_raw_data(raw_data, key, format_date_time)
    
    assert len(trans_data) == 20
    for row in trans_data:
        assert expected_transformed_data == row

    # load test.csv data
    create_db_tables(conn, cur)
    boole_2, line_count = load_data_into_database(trans_data, conn, cur, key, return_id)

    assert line_count == 20
    assert boole_2 == True