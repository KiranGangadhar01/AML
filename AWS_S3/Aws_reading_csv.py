import boto3
import os
from io import StringIO

bucket_name = 'wafer-fault--detection'


def aws_read_csv(filename):
    client = boto3.client('s3', aws_access_key_id=os.getenv("access_key"),
                          aws_secret_access_key=os.getenv("secret_key"))

    object_key = filename

    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')

    return StringIO(csv_string)


def aws_write_csv(df, filepath):
    s3_resource = boto3.resource('s3', aws_access_key_id=os.getenv("access_key"),
                                 aws_secret_access_key=os.getenv("secret_key"))
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=None, header=True)
    s3_resource.Object(bucket_name, filepath).put(Body=csv_buffer.getvalue())


# def read_csv(filename, destination):
#     s3 = boto3.resource('s3',
#                           aws_access_key_id = access_key,
#                           aws_secret_access_key = secret_key)
#
#     source_path = 'Training_Batch_Files/' + filename
#     destination_path = destination + filename
#
#     copy_source = {
#         'Bucket': 'wafer-fault--detection',
#         'Key': 'Training_Batch_Files/Wafer_07012020_223345.csv'
#     }
#     s3.meta.client.copy(copy_source, 'wafer-fault--detection', destination_path)