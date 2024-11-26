import boto3
import json

def lambda_handler(event, context):
    # Entrada
    bucket_name = event['body']['bucket_name']

    reg = 'us-east-1'  # Especifica la región aquí
    
    # Inicializa el cliente de S3 con la región especificada
    s3 = boto3.client('s3', region_name=reg)
    
    try:
        # Si la región es us-east-1, no se incluye LocationConstraint
        if reg == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': reg}
            )
        
        # Salida
        return {
            'statusCode': 200,
            'body': json.dumps(f'Bucket {bucket_name} creado exitosamente en la región {reg}.')
        }
    
    except Exception as e:
        # Manejo de errores
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error al crear el bucket: {str(e)}')
        }
