import os
from flask import Flask, render_template, request, redirect, send_file
from updowns3 import upload_to_aws, get_all_s3_keys, get_all_s3_buckets, download_from_aws

app = Flask(__name__)
UPLOAD_FOLDER = "."
BUCKET = "supportmeli"

@app.route('/')
def entry_point():
    return 'Test API'

@app.route("/storage")
def storage():
    contents = get_all_s3_keys("supportmeli")
    return contents

@app.route("/upload/<filename>", methods=['POST'])
def upload(filename):
    if request.method == "POST":
        output= upload_to_aws(filename, BUCKET)

        return "Upload complete"

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_from_aws(BUCKET,filename)

        return "Download complete"
        
if __name__ == '__main__':
    app.run(debug=True)