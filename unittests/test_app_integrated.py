from src.app.lambda_function import lambda_handler
from unittest.mock import Mock
from moto import mock_s3
import boto3

# Arrange mock S3 bucket with data 
BUCKET_NAME = 'test_bucket'
FILE_NAME = 'generation_uk_final_project_kahlail/unittests/test.csv'
FILE_LOCATION = FILE_NAME

