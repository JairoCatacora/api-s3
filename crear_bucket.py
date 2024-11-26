import boto3
import json

def lambda_handler(event, context):
    # Entrada
    bucket_name = event['body']['bucket_name']
    
    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)  # Crear el bucket
    
    # Salida
    return {
        'statusCode': 200,
        'body': json.dumps(f'Bucket {bucket_name} creado exitosamente.')
    }
