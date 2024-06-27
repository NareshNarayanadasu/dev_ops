To connect AWS RDS and S3 with a Lambda function that automatically updates the RDS database whenever a CSV file is uploaded to S3, you can follow these steps:

Set Up Your AWS Environment:

Create an S3 bucket.
Create an RDS instance (e.g., MySQL, PostgreSQL).
Create a Lambda function.
Configure S3 Bucket Notification:

Set up an event notification on the S3 bucket to trigger the Lambda function when a new CSV file is uploaded.
Lambda Function Configuration:

Assign an IAM role to the Lambda function with the necessary permissions to access S3 and RDS.
Write the Lambda function code to read the CSV file from S3, parse it, and update the RDS database.
Here is a step-by-step guide:

Step 1: Set Up S3 Bucket
Go to the S3 console and create a new bucket.
Note the bucket name as you'll need it later.
Step 2: Set Up RDS Instance
Go to the RDS console and create a new database instance.
Note the database endpoint, username, and password.
Step 3: Create Lambda Function
Go to the Lambda console and create a new Lambda function.
Choose a runtime (e.g., Python 3.8).
Step 4: Configure S3 Bucket Notification
In the S3 console, go to the bucket's properties.
Under "Event notifications," add a new notification.
Choose "All object create events" or specify the suffix .csv.
Select "Send to Lambda Function" and choose the Lambda function you created.
Step 5: Set IAM Role for Lambda
Go to the IAM console and create a new role.
Attach the following policies to the role:
AmazonS3ReadOnlyAccess
AmazonRDSFullAccess
AWSLambdaBasicExecutionRole
Attach this role to your Lambda function.
Step 6: Write Lambda Function Code
Below is an example Python code for the Lambda function:

python
Copy code
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
    }
Step 7: Set Environment Variables for Lambda
Go to the Lambda function's configuration.
Under "Environment variables," set the following variables:
RDS_HOST
RDS_USERNAME
RDS_PASSWORD
RDS_DB_NAME
Step 8: Test the Setup
Upload a CSV file to the S3 bucket.
Check the Lambda function logs to ensure it's triggered and processing the file.
Verify that the data is updated in the RDS database.
This setup ensures that every time a CSV file is uploaded to the specified S3 bucket, the Lambda function will be triggered, read the CSV file, and update the RDS database accordingly.


doc by naresh

