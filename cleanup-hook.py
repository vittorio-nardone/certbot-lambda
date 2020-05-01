#!/usr/bin/env python3

import os
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def delete_file(bucket, object_name):
    # Delete the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.delete_object(Bucket=bucket, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def cleanup_auth():
    ''' Remove token file used in validation.
        S3 Bucket name and cert domain must be the same!
    '''
    s3object = ".well-known/acme-challenge/" + os.environ['CERTBOT_TOKEN']
    delete_file(os.environ['CERTBOT_DOMAIN'], s3object)

if __name__ == "__main__":
    cleanup_auth()