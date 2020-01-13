# Bucketservice
Downlad/upload files in bucket s3

### requirements:
- python modules:

`boto3`
`Flask`
`pyfiglet`
`json`
`requests`

# Usage:
#TOOL MODE:

Create a `config.json` file with the `ACCESS_KEY`, `SECRET_KEY` , `BUCKET` , `LOCAL_PATH` and `URL`

Example:

``{
"ACCESS_KEY":"IAM USER",
"SECRET_KEY":"IAM SECRET",
"BUCKET":"BUCKET NAME",
"LOCAL_PATH":"LOCAL PATH",
"URL":"URL"
}``

- IMPORTANT: 
If no key is used. use only quotes in the values
 

### Arguments 

Help: `[-h]`

- To download: `[-d] [file] [bucket]`

- To upload:`[-u] [file] [bucket]`   (in the server, delete the lines 35,36 and 37 `r = requests.get(URL + "files/"+ sys.argv[2]
            	, data=json.dumps(data), headers=headers)
            print(r.text)`

- To show menu: `[-m]`

### Example:


`tool.py -d test.txt myawsbucket`

(If the bucket is in the .json file omit the bucket argument)

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

note: 

- Install python modules in the server.

- Run serverapi.py in the server.

- To List files in the bucket 

 `get url/files`

 in the json request body:

 `{
	"BUCKET" : "bucket name",
	"ACCESS_KEY" : "access key",
	"SECRET_KEY" : "secret key",}`


- To download file 

 `GET url/files/<file to donwload>`

 	note: the files will be downloaded in the same location of the script

in the json request body:

`{"BUCKET" : "bucket name",
	"ACCESS_KEY" : "access key",
	"SECRET_KEY" : "secret key"
}`

- To upload file

 `POST url/files/<file to upload>`

 	note: the files must be in the same location as the script

 in the json request body:

 `{"BUCKET" : "bucket name",
	"ACCESS_KEY" : "access key",
	"SECRET_KEY" : "secret key"
}`



