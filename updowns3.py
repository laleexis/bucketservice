import boto3
from os import listdir

#funciones
def client(ACCESS_KEY,SECRET_KEY):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
    return s3

def resource(ACCESS_KEY,SECRET_KEY):
    s3r = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    return s3r

def ls(route=""):
    files = {}
    cont = 1
    for f in listdir(route):
        files[cont] = f
        cont +=1
    return files

def upload_to_aws(local_file, bucket,s3filename,ACCESS_KEY,SECRET_KEY):
    s3 = client(ACCESS_KEY,SECRET_KEY)
    s3.upload_file(local_file, bucket, s3filename)
    print("Upload Successful")

def get_all_s3_buckets(ACCESS_KEY,SECRET_KEY):
    s3 = client(ACCESS_KEY,SECRET_KEY)
    response = s3.list_buckets()
    bucketdict = {}
    cont = 1
    for bucket in response['Buckets']:
        bucketdict[cont] = bucket['Name']
        cont+=1
   
    print("Listing buckets...")
    return bucketdict
def get_all_s3_keys(bucket,ACCESS_KEY,SECRET_KEY):
    s3 = client(ACCESS_KEY,SECRET_KEY)
    keys = []
    keysdict = {}
    cont = 1
    for key in s3.list_objects(Bucket=bucket)['Contents']:
        keys.append("["+str(cont)+"] "+key['Key'])
        keysdict[cont]= key['Key']
        cont=cont+1
    return keysdict
def delete_from_aws(bucket,key,ACCESS_KEY,SECRET_KEY):
    s3r= resource(ACCESS_KEY,SECRET_KEY)
    s3r.Object(bucket,key).delete()
    print("delete Successful")
    return ("deleted")

def download_from_aws(key,bucket,path,ACCESS_KEY,SECRET_KEY):
    s3r= resource(ACCESS_KEY,SECRET_KEY)
    output = f"{path}{key}"
    s3r.Bucket(bucket).download_file(key, output)

    return output
