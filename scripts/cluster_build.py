#!/usr/bin/env python
'''
demo script to show how to create an ASG of servers behind a ELB
'''

import boto3

client = boto3.client('autoscaling')

# various variables to define server stack being created
# need ImageId, MinCount, MaxCount, InstanceType, vpcId, etc
region_name = 'us-west-1'
network_vpc = 'vpc-23ba6646'
image_id = 'ami-37186257'
sec_group = ['sg-7aaa661e']
instance_type = 't2.micro'
key_name = 'ted'
elb_name = ['demotest']


# create autoscaling launch configuration template
client.create_launch_configuration(LaunchConfigurationName='testlaunch',
                                   ImageId=image_id,
                                   KeyName=key_name,
                                   SecurityGroups=sec_group,
                                   InstanceType=instance_type)

# create an autoscaling group using the pre-defined launch configuration
client.create_auto_scaling_group(AutoScalingGroupName='test1',
                                 MinSize=3,
                                 MaxSize=3,
                                 LoadBalancerNames=elb_name,
                                 LaunchConfigurationName='testlaunch',
                                 VPCZoneIdentifier='subnet-380ab85d')
