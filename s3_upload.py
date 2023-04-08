import os
import boto3
import re

s3 = boto3.client('s3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

bucket_name = 'terraformtemplatesnew'
file_name = r'c:/users/sr/Desktop/aws/s3_project/list-all-ec2.py'

def upload_s3():
    with open(file_name, 'rb') as f:
        filename = re.search('[^/]*$', file_name).group()
        s3.upload_fileobj(f, bucket_name, filename)
    return f"file {filename} has been upload successfully"

a=upload_s3()
print(a)