# Bucketservice
Downlad/upload files in bucket s3

### requirements:

`boto3`
`Flask`

`pyfiglet` (optional for tool mode)

# Usage:
#TOOL MODE:

Create a `.json` file with the `ACCESS_KEY`, `SECRET_KEY` , `BUCKET`(optional) and `LOCAL_PATH`(optional)

Example:

``{
"ACCESS_KEY":"IAM USER",
"SECRET_KEY":"IAM SECRET",
"BUCKET":"BUCKET NAME",
"LOCAL_PATH":"LOCAL PATH"
}``
 

### Arguments 

Help: `[-h]`

- To download: `[-d] [file] [bucket]`

- To upload:`[-u] [file] [bucket]`

- To show menu: `[-m]`

### Example:


`tool.py -d test.txt myawsbucket`

(If the bucket is declared in the .json file omit the bucket argument)

### Example

`tool.py -u test.txt'`


In the .json file:

`"BUCKET":"myawsbucket"`



### Menu:
### Download

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

### Delete:

- Run the script and enter option 2 `Delete file`

# API

- Run api.py in the server.

- To List files in the bucket 

 `POST url/files`

 in the json request body:

 `{
	"BUCKET" : "bucket name",
	"ACCESS_KEY" : "access key",
	"SECRET_KEY" : "secret key",}`


- To download file 

 `GET url/files`

- To upload file

 `POST url/files/upload`

 in the json request body:

 `{"BUCKET" : "bucket name",
	"ACCESS_KEY" : "access key",
	"SECRET_KEY" : "secret key",
	"UPLOAD" : "local path",
	"NAME" : "test.xslx"	
}`



