import boto3
import json
from botocore.exceptions import NoCredentialsError, ClientError
import botocore
from os import listdir

#crear un json con los datos
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print(data["ACCESS_KEY"])

ACCESS_KEY = data["ACCESS_KEY"]
SECRET_KEY = data["SECRET_KEY"]
BUCKET = data["BUCKET"]
LOCAL_PATH = data["LOCAL_PATH"]

print(" Menu: \n1 Upload file\n2 Download file")
selection = int(input("Select option"))

def ls(ruta=""):
    return listdir(ruta)

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
def download_from_aws(bucket,key,key):
    try:
        s3.Bucket(bucket).download_file(key,key)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise



if selection == 1:

    print(ls(LOCAL_PATH))
    LOCAL_FILE = input(str("Select file to upload"))
    S3_FILENAME= LOCAL_FILE

    print("Uploading file")
    uploaded = upload_to_aws(LOCAL_FILE, BUCKET, S3_FILENAME)

elif selection == 2:
    print("listing files...")
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    print(s3.list_objects_v2(Bucket=BUCKET))
    print(get_all_s3_keys(BUCKET))
    KEY = str(input("enter key"))

    s3 = boto3.resource('s3',
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

    download_from_aws(BUCKET,KEY,KEY)

else:
    print("wrong option")
