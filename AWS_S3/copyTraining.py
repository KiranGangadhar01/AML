import boto3
import os
from application_logging.logger import App_Logger

s3 = boto3.resource('s3',
                          aws_access_key_id = os.getenv("access_key"),
                          aws_secret_access_key = os.getenv("secret_key"))


def awscopy(filename, destination):
    # s3 = boto3.resource('s3',
    #                       aws_access_key_id = access_key,
    #                       aws_secret_access_key = secret_key)

    source_path = 'Training_Batch_Files/' + filename
    destination_path = destination + filename

    copy_source = {
        'Bucket': 'wafer-fault--detection',
        'Key': source_path
    }
    s3.meta.client.copy(copy_source, 'wafer-fault--detection', destination_path)


def awsdelete(filename, path):
    # s3 = boto3.resource('s3',
    #                       aws_access_key_id = access_key,
    #                       aws_secret_access_key = secret_key)

    delete_path = path + filename

    s3.Object('wafer-fault--detection', delete_path).delete()


def awsfolderdelete(path):
    bucket = s3.Bucket('wafer-fault--detection')
    logger = App_Logger()
    try:
        if len(list(bucket.objects.filter(Prefix="Training_Batch_Files/Bab_Folder/"))) > 0:
            bucket.objects.filter(Prefix=path).delete()
            file = "GeneralLog"
            logger.log(file, "BadRaw directory deleted before starting validation!!!")
    except Exception as e:
        file = "GeneralLog"
        logger.log(file, "Error while Deleting Directory : %s" % e)
        raise Exception
