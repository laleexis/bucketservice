#instalar libreria boto
import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

bucket_name = AWS_ACCESS_KEY_ID.lower() + "" #nombre del bucket con tu id + el nombre que quieras
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
location=boto.s3.connection.Location.DEFAULT) #crea el bucket con el bombre declarado en bucket_name

testfile = "" #ruta del archivo a subir
print ("Uploading %s to Amazon S3 bucket %s" % 
(testfile, bucket_name))

def percent_cb(complete, total):
	sys.stdout.write(".")
	sys.stdout.flush()


k = Key(bucket)
k.key = ""#nombre del arvhivo a subir
k.set_contents_from_filename(testfile,
cb=percent_cb, num_cb=10)	
print("test")