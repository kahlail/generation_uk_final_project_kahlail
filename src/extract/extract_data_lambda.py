import json
import os
import boto3
import csv

def extract_csv(bucket, key):
    try:
        print(f'extract_csv started, key = {key}')

        s3_resource = boto3.resource('s3')
        s3_object = s3_resource.Object(bucket,key)
        
        data = s3_object.get()['Body'].read().decode('utf-8').splitlines()
        reader = csv.reader(data)
        
        new_data = []

        for row in reader:
            new_data.append({'Date Time': row[0], 'Location': row[1], 'Name': row[2], 'Order': row[3], 'Total': row[4],'Payment Method': row[5], 'Card No': row[6]})
        
        print(f'extract_csv data succesfully extracted, key = {key} number of rows = {len(new_data)}')
        return new_data
   
    except Exception as e:
        print(f'extract_csv extraction failed key = {key}: {e}')
