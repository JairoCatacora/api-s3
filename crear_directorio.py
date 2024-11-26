import boto3
import json

def lambda_handler(event, context):
    # Entrada
    bucket_name = event['body']['bucket_name']
    directory_name = event['body']['directory_name']
    
    # Proceso
    s3 = boto3.client('s3')
    
    s3.put_object(Bucket=bucket_name, Key=f'{directory_name}/')
    
    # Salida
    return {
        'statusCode': 200,
        'body': json.dumps(f'Directorio "{bucket_name}/{directory_name}/" creado exitosamente.')
    }
