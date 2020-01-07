from flask import Flask, request
from updowns3 import upload_to_aws, get_all_s3_keys, get_all_s3_buckets, download_from_aws, delete_from_aws

app = Flask(__name__)
UPLOAD_FOLDER = "."
BUCKET = "supportmeli"

@app.route('/')
def entry_point():
    return 'Test API'

@app.route("/storage")
def storage():
    contents = get_all_s3_keys(BUCKET)
    return contents

@app.route("/upload/<filename>", methods=['POST'])
def upload(filename):
    if request.method == "POST":
        output= upload_to_aws(filename, BUCKET,filename)

        return "Upload complete"

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_from_aws(BUCKET,filename,filename)

        return "Download complete"
@app.route("/delete/<filename>", methods=['DELETE'])
def delete(filename):
	if request.method == 'DELETE':
		output = delete_from_aws(BUCKET,filename)
		return "Deleted"
        
if __name__ == '__main__':
    app.run(debug=True)