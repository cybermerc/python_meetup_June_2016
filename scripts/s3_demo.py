#!/usr/bin/env python
'''
demo script to show how to utilize s3 file viewer and uploader
'''

import boto3

menu = {'1': 'show bucket objects', '2': 'upload file'}

while True:
    options = menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    selection = raw_input('Please Select:')
    if selection == '1':
        s3 = boto3.client('s3')
        buckit = raw_input('input bucket name:')
        for key in s3.list_objects(Bucket=buckit)['Contents']:
            print(key['Key'])
    if selection == '2':
        s3 = boto3.resource('s3')
        buckit = raw_input('input bucket name:')
        obj = raw_input('input object name:')
        data = open(obj, 'rb')
        s3.Bucket(buckit).put_object(Key=obj, Body=data)
