import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    bucket_name = event['body']['bucket_name']

    try:
        response = s3_client.create_bucket(Bucket=bucket_name)
        
        return {
            'statusCode': 200,
            'body': f'Bucket "{bucket_name}" created successfully.',
            'response': str(response)
        }
    except ClientError as error:
        return {
            'statusCode': 400,
            'body': f'Error creating bucket: {error.response["Error"]["Message"]}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Unexpected error: {str(e)}'
        }
