import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    
    # Extrair ID e tipo dos recursos do evento
    resources = event['detail']['resources']
    
    # Definir tags a serem aplicadas
    tags = [
        {'Key': 'Ambiente', 'Value': 'Producao'},
        {'Key': 'Dono', 'Value': 'Geraldo'}
    ]
    
    # Aplicar tags aos recursos
    for resource in resources:
        client.create_tags(
            Resources=[resource['resourceId']],
            Tags=tags
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Tags aplicadas com sucesso!')
    }
