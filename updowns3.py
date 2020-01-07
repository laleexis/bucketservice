import boto3
import json
from botocore.exceptions import NoCredentialsError, ClientError
import botocore
from os import listdir
import pyfiglet
import sys


with open("config.json") as json_data_file:
        data = json.load(json_data_file)
ACCESS_KEY = data["ACCESS_KEY"]
SECRET_KEY = data["SECRET_KEY"]
LOCAL_PATH = data["LOCAL_PATH"]

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
s3r = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

#funciones
def ls(route=""):
    files = {}
    cont = 1
    for f in listdir(route):
        files[cont] = f
        cont +=1
    return files

def upload_to_aws(local_file, bucket,s3filename):
    try:
        s3.upload_file(local_file, bucket, s3filename)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def get_all_s3_buckets():
    response = s3.list_buckets()
    bucketdict = {}
    cont = 1
    for bucket in response['Buckets']:
        bucketdict[cont] = bucket['Name']
        cont+=1
   
    print("Listing buckets...")
    return bucketdict
def get_all_s3_keys(bucket):
    keys = []
    keysdict = {}
    cont = 1
    for key in s3.list_objects(Bucket=bucket)['Contents']:
        keys.append("["+str(cont)+"] "+key['Key'])
        keysdict[cont]= key['Key']
        cont=cont+1
    return keysdict
def delete_from_aws(bucket,key):
    s3r.Object(bucket,key).delete()
    print("delete Successful")
    return ("deleted")

def download_from_aws(bucket,key,s3key):
    try:
        s3r.Bucket(bucket).download_file(key,key)
        print("Download Successful")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
if len(sys.argv) ==1:
    print("modo API")

#Modo por parametros
else:
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
        print(" To download:  [-d] [file] [bucket]\n To upload: [-u] [file] [bucket]\n To show menu: [-m]")

    elif sys.argv[1]=="-m":
        ascii_banner = pyfiglet.figlet_format("DOWN&UPS3")
        print(ascii_banner)
#Modo menu
#crear un json con los datos   
        BUCKET = data["BUCKET"]
        print(" Menu: \n1 Upload file\n2 Download file\n3 Delete file")
        selection = int(input("Select option: "))

        if selection == 1:
            print("Listing files..")
            listf = ls(LOCAL_PATH)
            print(listf)
            s3name= int(input("Select file to upload: "))
            S3_FILENAME= listf[s3name]
            LOCAL_FILE = str(LOCAL_PATH)+ listf[s3name]
            S3_FILENAME= listf[s3name]
            bucketdown = get_all_s3_buckets()
            print(bucketdown)
            BUCKETSEL= int(input("Select Bucket: "))
            print("Uploading file...")
            uploaded = upload_to_aws(LOCAL_FILE, bucketdown[BUCKETSEL], S3_FILENAME)

        elif selection == 2:
            bucketdown = get_all_s3_buckets()
            print(bucketdown)
            BUCKETSEL= int(input("Select Bucket: "))
            keysdown = get_all_s3_keys(bucketdown[BUCKETSEL])
            print(keysdown)
            KEY = int(input("enter key: "))
            download_from_aws(bucketdown[BUCKETSEL],keysdown[KEY],keysdown[KEY])

        elif selection == 3:
            bucketdown = get_all_s3_buckets()
            print(bucketdown)
            BUCKETSEL= int(input("Select Bucket: "))
            keysdown = get_all_s3_keys(bucketdown[BUCKETSEL])
            print(keysdown)
            KEY = int(input("enter key: "))
            delete_from_aws(bucketdown[BUCKETSEL],keysdown[KEY],)

        else:
            print("wrong option")
    else:
        print(" To download:  [-d] [file] [bucket]\n To upload: [-u] [file] [bucket]\n To show menu: [-m]")        
