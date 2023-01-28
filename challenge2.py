import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
import pandas as pd

InstanceId = []
InstanceType = []
LaunchTime = []
AvailabilityZone = []
State = []
PrivateDnsName = []
PrivateIpAddress = []
PublicDnsName = []
PublicIpAddress = []
VolumeId = []
VpcId = []
response = client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["State"])
        InstanceId.append(instance["InstanceId"])
        InstanceType.append(instance["InstanceType"])
        LaunchTime.append(instance["LaunchTime"])
        AvailabilityZone.append(instance["Placement"]["AvailabilityZone"])
        State.append(instance["State"]["Name"])
        if instance["State"]["Name"] in 'running':
            PrivateDnsName.append(instance["PrivateDnsName"])
            PrivateIpAddress.append(instance["PrivateIpAddress"])
            PublicDnsName.append(instance["PublicDnsName"])
            PublicIpAddress.append(instance["PublicIpAddress"])
            VpcId.append(instance["VpcId"])
            for device in instance["BlockDeviceMappings"]:
                VolumeId.append(device["Ebs"]["VolumeId"])
        elif instance["State"]["Name"] in 'terminated':
            PrivateDnsName.append(["NA"])
            PrivateIpAddress.append(["NA"])
            PublicDnsName.append(["NA"])
            PublicIpAddress.append(["NA"])
            VpcId.append(["NA"])
            VolumeId.append(["NA"])
        else:
            PrivateDnsName.append(["NA"])
            PrivateIpAddress.append(["NA"])
            PublicDnsName.append(["NA"])
            PublicIpAddress.append(["NA"])
            VpcId.append(["NA"])
            for device in instance["BlockDeviceMappings"]:
                VolumeId.append(device["Ebs"]["VolumeId"])
            print(InstanceId)

server_report = pd.DataFrame(
    {'Instance_Id': InstanceId,
     'Instance_Type': InstanceType,
     'Availability': AvailabilityZone,
     'State': State,
     'PrivateDnsName': PrivateDnsName,
     'PrivateIpAddress': PrivateIpAddress,
     'PublicDnsName': PublicDnsName,
     'PublicIpAddress': PublicIpAddress,
     'VpcId': VpcId,
     'VolumeId': VolumeId
     })


json = server_report.to_json()
print(json)
