#!/usr/bin/env python
'''
demo script to show how to create a group of servers behind a ELB
'''

import boto3

# various variables to define server stack being created
# need ImageId, MinCount, MaxCount, InstanceType, vpcId, etc
region_name = ''
network_vpc = ''
image_id = ''
min_srv = ''
max_srv = ''
instance_type = ''
key_name = ''
