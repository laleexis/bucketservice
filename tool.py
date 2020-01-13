from updowns3 import *
import sys
import pyfiglet
import json
import requests

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

ACCESS_KEY = data["ACCESS_KEY"]
SECRET_KEY = data["SECRET_KEY"]
LOCAL_PATH = data["LOCAL_PATH"]
BUCKET = data["BUCKET"]
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)
s3r = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
me = " To download:  [-d] [file] [bucket]\n To upload: [-u] [file] [bucket]\n To show menu: [-m]"
# api endpoint
URL = "http://3.15.23.57/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {
    "ACCESS_KEY": ACCESS_KEY,
    "SECRET_KEY": SECRET_KEY,
    "BUCKET": sys.argv[3],
    "LOCAL_PATH": LOCAL_PATH,
}


def menu(s3, s3r, me):
    if sys.argv[1] == "-u":
        print("Uploading Files")
        if len(sys.argv) == 3:
            upload_to_aws(sys.argv[2], data["BUCKET"], sys.argv[2], ACCESS_KEY, SECRET_KEY)
        else:
            upload_to_aws(sys.argv[2], sys.argv[3], sys.argv[2], ACCESS_KEY, SECRET_KEY)
            r = requests.get(URL + "files"#+ sys.argv[2]
            	, data=json.dumps(data), headers=headers)
            print(r.text)
    elif sys.argv[1] == "-d":
        if len(sys.argv) == 3:
            download_from_aws(sys.argv[2], data["BUCKET"], ACCESS_KEY, SECRET_KEY)

        else:
            download_from_aws(sys.argv[2], sys.argv[3], ACCESS_KEY, SECRET_KEY)

    elif sys.argv[1] == "-h":
        print(me)

    elif sys.argv[1] == "-m":
        ascii_banner = pyfiglet.figlet_format("DOWN&UPS3")
        print(ascii_banner)
        # Modo menu
        # crear un json con los datos
        BUCKET = data["BUCKET"]
        print(" Menu: \n1 Upload file\n2 Download file\n3 Delete file")
        selection = int(input("Select option: "))

        if selection == 1:
            print("Listing files..")
            listf = ls(LOCAL_PATH)
            print(listf)
            s3name = int(input("Select file to upload: "))
            S3_FILENAME = listf[s3name]
            LOCAL_FILE = str(LOCAL_PATH) + listf[s3name]
            S3_FILENAME = listf[s3name]
            bucketdown = get_all_s3_buckets(ACCESS_KEY, SECRET_KEY)
            print(bucketdown)
            BUCKETSEL = int(input("Select Bucket: "))
            print("Uploading file...")
            upload_to_aws(LOCAL_FILE, bucketdown[BUCKETSEL], S3_FILENAME, ACCESS_KEY, SECRET_KEY)

        elif selection == 2:
            bucketdown = get_all_s3_buckets(ACCESS_KEY, SECRET_KEY)
            print(bucketdown)
            BUCKETSEL = int(input("Select Bucket: "))
            keysdown = get_all_s3_keys(bucketdown[BUCKETSEL], ACCESS_KEY, SECRET_KEY)
            print(keysdown)
            KEY = int(input("enter key: "))
            download_from_aws(keysdown[KEY], bucketdown[BUCKETSEL], ACCESS_KEY, SECRET_KEY)

        elif selection == 3:
            bucketdown = get_all_s3_buckets(ACCESS_KEY, SECRET_KEY)
            print(bucketdown)
            BUCKETSEL = int(input("Select Bucket: "))
            keysdown = get_all_s3_keys(bucketdown[BUCKETSEL], ACCESS_KEY, SECRET_KEY)
            print(keysdown)
            KEY = int(input("enter key: "))
            delete_from_aws(bucketdown[BUCKETSEL], keysdown[KEY], ACCESS_KEY, SECRET_KEY)

        else:
            print("wrong option")
    else:
        print(me)


menu(s3, s3r, me)
