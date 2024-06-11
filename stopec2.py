from _future_ import print_function
from botocore.exceptions import ClientError
import boto3
import json
import os

def handler(event, context):
  try:
    ec2 = boto3.client('ec2')
    instanceID = os.environ['INSTANCE_ID']
    response = ec2.stop_instances(
          InstanceIds=[
              instanceID,
          ],
    )
  except ClientError as e:
    print(e)
  return response
