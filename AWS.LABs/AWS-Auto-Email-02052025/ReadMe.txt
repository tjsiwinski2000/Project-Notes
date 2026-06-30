SUMMARY
- use multiple services together to send [marketing emails]


VIDEO
- https://www.youtube.com/watch?v=hK0ztmWCBA8&list=PLwyXYwu8kL0wMalR9iXJIPfiMYWNFWQzx&index=8


SES [simple email service]
Lambda [sending logic]
AWS Event Bridge [scheduler]
IAM [make sure have access to do things in the other services]
S3  
- tttt-email-marketing1965
- [e-mail templates in ".html" files] 

Lambda Function
- "munges" e-mail template and CSV file [inside the code] and SES service
# Initialize the boto3 client [boto is python SDK for AWS]
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')
- from email ?? Source='tjsiwinski_2000@yahoo.com',  # Replace with your verified "From" address 
- should be from tjsiwinski.com domain? FUZZY here 

[PERMISSIONS WITH Lambda]
- access denied S3, SES demonstrated
- When Lambda created, execution role [created during creation] only allows writing to CLOUD WATCH LOGS
- Created policy [via JSON she provided]
- Attached [NEWLY CREATED] policy to execution role

[EVENT Bridge]
- formerly cloud watch events ; allows for scheduled jobs
- creating a new schedules requires creating a new role for the schedule [take the DEFAULTS]
- to see if Lambda Ran [goto LambdaFunction:Monitor:TimeZone..TimePeriod]
- NOTE: Link to cloudwatch logs [GOOD FIRST PLACE TO DO SOME TROUBLESHOOTING]
- IDEAS - addresses in dynamo db / UI button 
***left off 23:22 in the VIDEO
========================
Lambda Function Python Code

import boto3
import csv

# Initialize the boto3 client
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    # Specify the S3 bucket name
    bucket_name = 'tttt-email-marketing1965' # Replace with your bucket name

    try:
        # Retrieve the CSV file from S3
        csv_file = s3_client.get_object(Bucket=bucket_name, Key='contacts.csv')
        lines = csv_file['Body'].read().decode('utf-8').splitlines()
        
        # Retrieve the HTML email template from S3
        email_template = s3_client.get_object(Bucket=bucket_name, Key='email_template.html')
        email_html = email_template['Body'].read().decode('utf-8')
        
        # Parse the CSV file
        contacts = csv.DictReader(lines)
        
        for contact in contacts:
            # Replace placeholders in the email template with contact information
            personalized_email = email_html.replace('{{FirstName}}', contact['FirstName'])
            
            # Send the email using SES
            response = ses_client.send_email(
                Source='you@yourdomainname.com',  # Replace with your verified "From" address
                Destination={'ToAddresses': [contact['Email']]},
                Message={
                    'Subject': {'Data': 'Your Weekly Tiny Tales Mail!', 'Charset': 'UTF-8'},
                    'Body': {'Html': {'Data': personalized_email, 'Charset': 'UTF-8'}}
                }
            )
            print(f"Email sent to {contact['Email']}: Response {response}")
    except Exception as e:
        print(f"An error occurred: {e}")




Lambda Function Test Event

{
  "comment": "Generic test event for scheduled Lambda execution. The function does not use this event data.",
  "test": true
}



IAM Policy for SES and S3 permissions

Update the ARN to use your S3 bucket

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::ttt-email-marketing/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ses:SendEmail",
                "ses:SendRawEmail"
            ],
            "Resource": "*"
        }
    ]
}

