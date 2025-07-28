import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    
    # Extract instance ID from the EventBridge event
    instance_id = event['detail']['instance-id']
    
    # Get instance details
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_type = response['Reservations'][0]['Instances'][0]['InstanceType']
    
    # If the instance is NOT a t3.micro, stop it
    if instance_type != 't2.micro':
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} stopped because it is not a t2.micro.")
    
    return {
        'statusCode': 200,
        'body': f"Checked instance {instance_id}, action taken if needed."
    }
