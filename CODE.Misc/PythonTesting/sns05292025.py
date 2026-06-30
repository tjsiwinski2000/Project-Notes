import boto3

sns = boto3.client('sns', region_name='us-east-1')

response = sns.publish(
    PhoneNumber='+12107896843',
    Message='Hello from AWS SNS!'
)

print(response)