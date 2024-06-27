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
2. Under "Event notifications," add a new notification.
   - Choose "All object create events" or specify the suffix `.csv`.
   - Select "Send to Lambda Function" and choose the Lambda function you created.

## Step 5: Set IAM Role for Lambda

1. Go to the IAM console and create a new role.
2. Attach the following policies to the role:
   - AmazonS3ReadOnlyAccess
   - AmazonRDSFullAccess
   - AWSLambdaBasicExecutionRole
3. Attach this role to your Lambda function.

## Step 6: Write Lambda Function Code

Below is an example Python code for the Lambda function:

```python
import boto3
import csv
import pymysql
import os

# Initialize the S3 client
s3 = boto3.client('s3')

# Database settings
rds_host = os.environ['RDS_HOST']
rds_username = os.environ['RDS_USERNAME']
rds_password = os.environ['RDS_PASSWORD']
rds_db_name = os.environ['RDS_DB_NAME']

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download the file from S3
    s3.download_file(bucket, key, '/tmp/temp.csv')
    
    # Connect to the RDS database
    connection = pymysql.connect(
        host=rds_host,
        user=rds_username,
        password=rds_password,
        db=rds_db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            # Read the CSV file
            with open('/tmp/temp.csv', 'r') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Skip header row
                
                # Prepare the insert statement
                insert_statement = f"INSERT INTO your_table ({', '.join(header)}) VALUES ({', '.join(['%s'] * len(header))})"
                
                for row in csv_reader:
                    cursor.execute(insert_statement, row)
        
        connection.commit()
    
    finally:
        connection.close()

    return {
        'statusCode': 200,
        'body': f'Successfully processed {key} from {bucket}'
    } ```
# Lambda Trigger for RDS Setup

This guide will help you set up an AWS Lambda function that is triggered by an S3 bucket upload and updates an RDS database accordingly.

## Step 7: Set Environment Variables for Lambda

1. Go to the Lambda function's configuration.
2. Under "Environment variables," set the following variables:

   - `RDS_HOST` = `db-lambda-trigger.cluster-cf8mso6wgybr.us-east-1.rds.amazonaws.com`
   - `RDS_USERNAME` = `admin`
   - `RDS_PASSWORD` = `admin123`
   - `RDS_DB_NAME` = `<your-database-name>`

## Step 8: Test the Setup

1. **Upload a CSV file to the S3 bucket**:
   - Use the S3 bucket named `lambda-trigger-for-rds`.
   - Ensure the CSV file is in the correct format for processing.

2. **Check the Lambda function logs**:
   - Go to the AWS Lambda console.
   - Navigate to your Lambda function.
   - Check the logs in Amazon CloudWatch to ensure the function is triggered and processing the file.

3. **Verify the data in the RDS database**:
   - Connect to your RDS database.
   - Verify that the data from the CSV file has been correctly updated.

This setup ensures that every time a CSV file is uploaded to the specified S3 bucket, the Lambda function will be triggered, read the CSV file, and update the RDS database accordingly.
