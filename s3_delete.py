import boto3
import os


s3=boto3.resource("s3")

# creating a function that will objects from the s3
def s3_delete_object(bucketname,object_key):
    s3.Object(bucketname,object_key).delete()
    return object_key


# s3_delete_object("terraformtemplatesnew","newt.jpeg")

## creating a function that will delete the multiple objects from the s3
def s3_multiple_objects(bucketname,object_list):
    for key in range(len(object_list)):
        s3.Object(bucketname,object_list[key]).delete()
        print(f"file {object_list[key]} has been deleted")
    
    
o_list = ["hr-2.txt","i1.png","mypg.py"]
s3_multiple_objects("terraformtemplatesnew",o_list)

 