import json
import boto3

def autotagger(event, context):
    instance_id = (event['detail']['instance-id'])
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(instance_id)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    if "ftcxa" in instancename.lower():
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'teamDl', 'Value': 'euc@ft.com'},
                {'Key': 'environment', 'Value': 'p'},
                {'Key': 'systemCode', 'Value': 'citrixxendesktop'}
            ]
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
