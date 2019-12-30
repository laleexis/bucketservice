import boto3
from botocore.exceptions import NoCredentialsError, ClientError

import botocore

ACCESS_KEY = ''
SECRET_KEY = ''
BUCKET = ""
LOCAL_FILE = "uploadtest12.txt"
S3_FILENAME = LOCAL_FILE

print(" Menu: \n1 Upload file\n2 Download file")
selection = int(input("Select option"))


def upload_to_aws(local_file, bucket, s3_file):
    try:
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def get_all_s3_keys(bucket):
    keys = []

    kwargs = {'Bucket': bucket}
    while True:
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            keys.append(obj['Key'])

        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break

    return keys


if selection == 1:
    print("Uploading file")
    uploaded = upload_to_aws(LOCAL_FILE, BUCKET, S3_FILENAME)

elif selection == 2:
    print("Download files")
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    s3.list_objects_v2(Bucket=BUCKET)
    print(get_all_s3_keys(BUCKET))
    KEY = str(input("enter key"))  # replace with your object key

    s3 = boto3.resource('s3',
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

    try:
        s3.Bucket(BUCKET).download_file(KEY, KEY)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

else:
    print("wrong option")
