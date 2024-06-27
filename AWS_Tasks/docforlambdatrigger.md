# Automatically Update RDS Database with Lambda and S3

## Step 1: Set Up S3 Bucket

1. Go to the S3 console and create a new bucket.
2. Note the bucket name as you'll need it later.

## Step 2: Set Up RDS Instance

1. Go to the RDS console and create a new database instance.
2. Note the database endpoint, username, and password.

## Step 3: Create Lambda Function

1. Go to the Lambda console and create a new Lambda function.
2. Choose a runtime (e.g., Python 3.8).

## Step 4: Configure S3 Bucket Notification

1. In the S3 console, go to the bucket's properties.
2. Under "Event notifications," add a new notification:
   - Choose "All object create events" or specify the suffix `.csv`.
   - Select "Send to Lambda Function" and choose the Lambda function you created.

## Step 5: Set IAM Role for Lambda

1. Go to the IAM console and create a new role.
2. Attach the following policies to the role:
   - `AmazonS3ReadOnlyAccess`
   - `AmazonRDSFullAccess`
   - `AWSLambdaBasicExecutionRole`
3. Attach this role to your Lambda function.

## Step 6: Write Lambda Function Code

Below is a sample Lambda function code that reads a CSV file from S3 and updates an RDS database:

```python
import json
import boto3
import pymysql
import csv
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # RDS connection details
    rds_host = os.environ['RDS_HOST']
    rds_username = os.environ['RDS_USERNAME']
    rds_password = os.environ['RDS_PASSWORD']
    rds_db_name = os.environ['RDS_DB_NAME']
    
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Fetch the CSV file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    lines = response['Body'].read().decode('utf-8').split()
    
    # Connect to RDS
    connection = pymysql.connect(
        host=rds_host,
        user=rds_username,
        password=rds_password,
        db=rds_db_name
    )
    
    try:
        with connection.cursor() as cursor:
            csv_reader = csv.reader(lines)
            for row in csv_reader:
                sql = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
                cursor.execute(sql, tuple(row))
        connection.commit()
    finally:
        connection.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('CSV file processed successfully')
    }
