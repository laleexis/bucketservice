import boto3
from botocore.exceptions import NoCredentialsError
import botocore

ACCESS_KEY = 'AKIAVHP33H4XBGJBCYHB'
SECRET_KEY = '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'
BUCKET = "supportmeli"
LOCAL_FILE = "path local file"
S3_FILENAME = LOCAL_FILE

print(" Menu: \n1 Upload file\n2 Download dile")
selection = int(input("Select option"))


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


if selection == 1:
    print("Uploading file")
    uploaded = upload_to_aws(LOCAL_FILE, BUCKET, S3_FILENAME)

elif selection == 2:
    print("descarga de archivos")

    KEY = str(input("ingrese key"))  # replace with your object key

    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET).download_file(KEY, 'my_local_image.jpg')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

else:
    print("seleccione una opcion valida")
