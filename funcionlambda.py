import json
import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    # Nombre del bucket de S3 y de la imagen de prueba que subirás después
    bucket_name = "tu-bucket-de-imagenes-aws" 
    image_name = "foto.jpg"
    
    try:
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': image_name
                }
            },
            MaxLabels=10,
            MinConfidence=75
        )
        
        print("Características detectadas:")
        for label in response['Labels']:
            print(f"- {label['Name']} ({label['Confidence']:.2f}%)")
            
        return {
            'statusCode': 200,
            'body': json.dumps(response['Labels'])
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps("Error al procesar la imagen")
        }