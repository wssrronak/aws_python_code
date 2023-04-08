import boto3
import json
AWS_REGION="ap-south-1"

## it will list all ec2 instances:

def fetch_ec2_ids():
    EC2_Resource=boto3.resource('ec2',region_name=AWS_REGION)
    instances = EC2_Resource.instances.all()
    for i in instances:
        print(f"EC2 Instances : {i.id}")
        print(f"EC2 Instances state : {i.state['Name']}")
        # print(f"EC2 Instance platform : {i.platform}")
        print(f"="*50)

# fetch_ec2_ids()

## it will list all the security groups

def list_all_security_groups():
    ec2_resource=boto3.resource('ec2',region_name=AWS_REGION)
    sgs=ec2_resource.security_groups.all()
    for i in sgs:
        print("Security group id:", i.id)
    
# list_all_security_groups()



# list_all_security_groups()

def list_all_subnet_groups():
    ec2_resource=boto3.resource('ec2',region_name=AWS_REGION)
    sub_net=ec2_resource.subnet_groups.all()
    for i in sub_net:
        print(i.id)

# list_all_subnet_groups()

#filter_ec2_instances()

def start_ec2_instance():
    instance_id="i-0105d7536fa792951"
    ec2_resource=boto3.resource('ec2',region_name=AWS_REGION)
    instance=ec2_resource.Instance(instance_id)
    instance.start()
    print(f"EC2 instance with instance id : {instance_id} has succesffully started")


## starting ec2 instances
# start_ec2_instance()


## checking states of ec2 instances

def filter_ec2_instances(inst_stat):
    EC2_Resource=boto3.resource('ec2',region_name=AWS_REGION)  
    instance_state=inst_stat  
    # instance_state=input("Enter ur instance state: ")    
    instances=EC2_Resource.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                        instance_state
                ]
            }
        ]
    )
    print(f"Instance state showing for {instance_state} state")
    for i in instances:
        print(f"Instance ID: {i.id}")
        print('='*50)
        yield i.id


# filter_ec2_instances("running")



def stopped_instance():
    inst_stat=filter_ec2_instances("running")
    ec2_resource=boto3.resource('ec2',region_name=AWS_REGION)
    for i in inst_stat:
        instance=ec2_resource.Instance(i)
        print(f"Instance {i} will stop now")
        instance.stop()
        instance.wait_until_stopped()


# stopped_instance()

def filter_out_type(inst_type):
    EC2_Resource=boto3.resource('ec2',region_name=AWS_REGION)
    instance_type=inst_type
    instances=EC2_Resource.instances.filter(
        Filters = [
            {
                'Name': 'instance-type',
                'Values' : [ 
                            instance_type
                ]
            }
        ]
    )
    print(f"Instance running on {instance_type} type")
    print("*"*80)
    for i in instances:
        print("="*50)
        print(f"Instance Type: {i.id}")

# filter_out_type("t2.medium")


def list_ebs_volumes():
    ec2_resources=boto3.resource('ec2',region_name=AWS_REGION)
    instances=ec2_resources.instances.all()
    for i in instances:
        instance_id=i.id
        instance=ec2_resources.Instance(instance_id)
        device_map=instance.block_device_mappings
        print("="*50)
        print(f"Volume attach to the ec2 instance: {instance_id}")
        for dev in device_map:
            print(f"Volume {dev['Ebs']['VolumeId']} attached as {dev['DeviceName']}")
            


# list_ebs_volumes()

def list_all_tags():
    ec2_resource=boto3.resource('ec2',region_name=AWS_REGION)
    instance=ec2_resource.instances.all()
    for i in instance:
        instance_id = i.id
        instances=ec2_resource.instances.filter(
        Filters=[
            {
                "Name": "Instance ID",
                "Values": instance_id,
            }       
            ]
        )
        for j in instances:
            print(f"Ec2 Instance: {instance.id} tags: ")
            if len(j.tags) > 0:
                for tag in j.tags:
                    print(f"- Tag : {tag['Key']}={tag['Value']}")
            else:
                print(f'- No Tags')
            print("-"*60)

# list_all_tags()

## describing about security groups

def describe_sg():
    ec2_client=boto3.client('ec2',region_name=AWS_REGION)
    SECURITY_GROUP_ID ='sg-031ed77a64aa7b1f7'
    response=ec2_client.describe_security_groups(
        GroupIds=[
            SECURITY_GROUP_ID,
        ],
    )
    print(f"Security Group {SECURITY_GROUP_ID} attributes")
    for sg in response['SecurityGroups']:
        print(json.dumps(sg,indent=4))

describe_sg()
