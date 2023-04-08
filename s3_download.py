import boto3
import os

## creating a function that will going to download the files from the s3.

def s3_download(bucketname,file_key):
    # Create an S3 client
    s3 = boto3.client("s3", aws_access_key_id=os.environ["aws_access_key_id"], aws_secret_access_key=os.environ["aws_secret_access_key"])
    # Download the file from S3
    file_downloaded=s3.download_file(bucketname, file_key, file_key.split("/")[-1])
    return f"file {file_downloaded} has been downloaded"

## printing the name of the download file.
save=s3_download("terraformtemplatesnew","mypg.py")
print(save)