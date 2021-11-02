import boto3
import os


def aws_listfiles(prefix):
    s3 = boto3.resource('s3',
                          aws_access_key_id = os.getenv("access_key"),
                          aws_secret_access_key = os.getenv("secret_key"))

    bucket = s3.Bucket('wafer-fault--detection')
    filename = []

    for obj in bucket.objects.filter(Prefix=prefix):
        filename.append(obj.key.split('/')[-1])

    return filename

