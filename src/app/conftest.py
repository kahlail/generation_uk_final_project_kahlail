from moto import mock_s3
import boto3
import os
import pytest


# Mock AWS credentials
@pytest.fixture
def aws_credentials():
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        conn = boto3.client("s3", region_name="eu-west-1")
        yield conn

@pytest.fixture
def test_integrated_lambda_function(s3_client):
    # Mock AWS bucket and key using moto and test credentials
    bucket_name = 'test_bucket'
    key = 'test.csv'
    file_path = '/Users/User/Documents/CODING/GitHub_Profile/generation_uk_final_project_kahlail/unittests/test.csv'

    # Create the S3 bucket
    s3_client.create_bucket(Bucket=bucket_name)

    # Upload test.csv file to the mock bucket
    s3_client.upload_file(file_path, bucket_name, key)

    # Download the test.csv file
    download_path = '/tmp/test.csv'
    s3_client.download_file(bucket_name, key, download_path)

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

    with open(download_path, 'r') as file:
        raw_data = extract_csv(file)

        assert isinstance(raw_data, list)
        assert len(raw_data) == 20
        for row in raw_data:
            assert row == expected_raw_data

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
        assert row == expected_transformed_data

    # load test.csv data
    create_db_tables(conn, cur)
    boole_2, line_count = load_data_into_database(trans_data, conn, cur, key, return_id)

    assert line_count == 20
    assert boole_2 is True
