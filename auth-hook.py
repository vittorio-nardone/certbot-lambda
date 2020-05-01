#!/usr/bin/env python3

import os
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_auth():
    ''' Write token file and upload it to correct S3 bucket and folder
        S3 Bucket name and cert domain must be the same!
    '''
    f = open("/tmp/verification.txt", "w")
    f.write(os.environ['CERTBOT_VALIDATION'])
    f.close()

    s3object = ".well-known/acme-challenge/" + os.environ['CERTBOT_TOKEN']
    upload_file("/tmp/verification.txt", os.environ['CERTBOT_DOMAIN'], s3object)
    os.remove("/tmp/verification.txt")

if __name__ == "__main__":
    upload_auth()