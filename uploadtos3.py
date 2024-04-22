import os
import boto3
import logging
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region
    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).
    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client("s3")
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client("s3", region_name=region)
            location = {"LocationConstraint": region}
            s3_client.create_bucket(
                Bucket=bucket_name, CreateBucketConfiguration=location
            )
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_csv_to_s3(csv_file_path, bucket_name, object_key):
    """Upload a CSV file to an S3 bucket
    :param csv_file_path: Path to the CSV file
    :param bucket_name: Name of the S3 bucket
    :param object_key: Key (path) of the object in the bucket
    :return: True if successful, False otherwise
    """
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(csv_file_path, bucket_name, object_key)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Make sure to give a unique (non-existing) bucket name
bucket_name = "dsci6007finalprojectdata"
create_bucket(bucket_name)

# Path to the CSV file you want to upload
csv_file_path = "/home/ec2-user/rideshare_kaggle.csv"

# Key (path) of the object in the bucket
object_key = "rideshare_kaggle.csv"

# Upload the CSV file to S3
upload_csv_to_s3(csv_file_path, bucket_name, object_key)
