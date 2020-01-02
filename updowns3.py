import boto3
import json
from botocore.exceptions import NoCredentialsError, ClientError
import botocore
from os import listdir
import pyfiglet
import sys

ascii_banner = pyfiglet.figlet_format("DOWN/UP S3")
print(ascii_banner)
with open("config.json") as json_data_file:
        data = json.load(json_data_file)
ACCESS_KEY = data["ACCESS_KEY"]
SECRET_KEY = data["SECRET_KEY"]
LOCAL_PATH = data["LOCAL_PATH"]


#funciones
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

def get_all_s3_buckets():
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Listing buckets...")
    return buckets
def get_all_s3_keys(bucket):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
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
    print("Listing Files...")
    return keys
def download_from_aws(bucket,key,s3key):
    s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    try:
        s3.Bucket(bucket).download_file(key,key)
        print("Download Successful")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
if len(sys.argv) ==1:

#Modo menu
#crear un json con los datos   
    BUCKET = data["BUCKET"]
    
    print(" Menu: \n1 Upload file\n2 Download file")
    selection = int(input("Select option: "))

    if selection == 1:
        print("Listing files..")
        print(ls(LOCAL_PATH))
        s3name= input(str("Select file to upload: "))
        S3_FILENAME= s3name
        LOCAL_FILE = str(LOCAL_PATH)+ s3name
        S3_FILENAME= s3name
        print(LOCAL_FILE)
        print(get_all_s3_buckets())
        BUCKETSEL= str(input("Select Bucket: "))
        print("Uploading file...")
        uploaded = upload_to_aws(LOCAL_FILE, BUCKETSEL, S3_FILENAME)

    elif selection == 2:
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        print(get_all_s3_buckets())
        BUCKETSEL= str(input("Select Bucket: "))
        print(get_all_s3_keys(BUCKETSEL))
        KEY = str(input("enter key: "))
        download_from_aws(BUCKET,KEY,KEY)

    else:
        print("wrong option")
else:#Modo por parametros
    if sys.argv[1] == "-u":
        S3_FILENAME=sys.argv[2]
        print("Uploading Files")
        if len(sys.argv)==3:
            upload_to_aws(sys.argv[2],data["BUCKET"],sys.argv[2])
        else:
            uploaded = upload_to_aws(sys.argv[2], sys.argv[3], sys.argv[2])
    elif sys.argv[1]=="-d":
        if len(sys.argv)==3:
            download_from_aws(data["BUCKET"],sys.argv[2],sys.argv[2])
        else:
            download_from_aws(sys.argv[3],sys.argv[2],sys.argv[2])
    elif sys.argv[1]=="-h":
        print(" To download:  [-d] [file] [bucket]\n To upload: [-u] [file] [bucket]\n To show menu: no args" )
    else:
        print("select [-d] to donwload, [-u] to upload or none for show menu...")

