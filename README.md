# Bucketservice
Downlad/upload files in bucket s3

###requirements:

`boto3`

#Usage:



Create a `.json` file with the `ACCESS_KEY`, `SECRET_KEY` , `BUCKET`(optional) and `LOCAL_PATH`(optional)

Example:
``{
"ACCESS_KEY":"IAM USER",
"SECRET_KEY":"IAM SECRET",
"BUCKET":"BUCKET NAME",
"LOCAL_PATH":"LOCAL PATH"
}``
 
### Download:

### Arguments mode 

Help: `[-h]`

- To download: `[-d] [file] [bucket]`

- To upload:`[-u] [file] [bucket]`

- To show menu: no args

### Example:


`updowns3.py -d test.txt myawsbucket`

(If the bucket is declared in the .json file omit the bucket argument)

### Example

`updowns3.py -u test.txt'
In the .json file:
`"BUCKET":"myawsbucket"`

### Menu mode


- Run the script and enter option 2 `download file`

The buckets avilable Will be listed

- Enter the bucket

the files hosted in the bucket will be listed

- Enter the key you want to download

the file will be downloaded in the same location as the script

### Upload:

- Run the sctipt and enter option 2 `upload file`

The files hosted in local path will be listed

- Enter te file name yow want to upload

The file will be uploaded in the bucket 




