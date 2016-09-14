import boto3

client = boto3.client('sqs')

response = client.receive_message(
    QueueUrl='https://sqs.eu-west-1.amazonaws.com/164968468391/gymchecker',
    AttributeNames=[
        'All'
    ],
    MessageAttributeNames=[
        'All',
    ],
    MaxNumberOfMessages=1,
    VisibilityTimeout=123,
    WaitTimeSeconds=20
)

print (response)