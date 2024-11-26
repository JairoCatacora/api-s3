import boto3
import json
import base64

def lambda_handler(event, context):
    # Entrada
    bucket_name = event['body']['bucket_name']
    directory_name = event['body']['directory_name']
    file_name = event['body']['file_name']
    file_content = event['body']['file_content']
        
    file_data = base64.b64decode(file_content)
    
    # Proceso
    s3 = boto3.client('s3')
    object_key = f"{directory_name}/{file_name}"
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=file_data)
    
    # Salida
    return {
        'statusCode': 200,
        'body': json.dumps(f'Archivo "{file_name}" subido exitosamente en el directorio "{bucket_name}/{directory_name}/".')
    }
