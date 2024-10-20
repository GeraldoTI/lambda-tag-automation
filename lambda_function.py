import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    
    # Extrai o ID da instância do evento CloudTrail
    instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
    
    # Define as tags a serem aplicadas
    tags = [
        {'Key': 'Owner', 'Value': 'DevOpsTeam'},
        {'Key': 'Environment', 'Value': 'Production'},
        {'Key': 'Project', 'Value': 'Automation'}
    ]
    
    # Aplica as tags à instância EC2
    ec2_client.create_tags(Resources=[instance_id], Tags=tags)
    
    return f"Tags applied to instance {instance_id}"
