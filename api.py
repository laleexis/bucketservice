from flask import Flask, request, send_file
from updowns3 import upload_to_aws, get_all_s3_keys, get_all_s3_buckets, download_from_aws, delete_from_aws

app = Flask(__name__)
UPLOAD_FOLDER = "."
BUCKET = "supportmeli"
path = "C:/Users/alucero/Documents"


@app.route('/')
def entry_point():
    return 'Test API'


@app.route("/files", methods=['POST'])  # json in body
def storage():
    req_data = request.get_json()
    if request.method == "POST":
        contents = get_all_s3_keys(req_data['BUCKET'], req_data['ACCESS_KEY'], req_data['SECRET_KEY'])
        return contents


@app.route("/files/upload", methods=['POST'])
def upload():
    req_data = request.get_json()
    if request.method == "POST":
        output = upload_to_aws(req_data['UPLOAD'], req_data['BUCKET'], req_data['NAME'], req_data['ACCESS_KEY'],
                               req_data['SECRET_KEY'])
        return "Upload complete"


@app.route("/files/<filename>", methods=['POST'])
def download(filename):
    if request.method == 'GET':
        request_data = request.get_json()
        download_from_aws(request_data["S3_KEY"], request_data["BUCKET"], request_data["PATH_SV"],request_data["ACCESS_KEY"],request_data["SECRET_KEY"])
        return "ok"


@app.route("/files/<filename>", methods=['DELETE'])
def delete(filename):
    if request.method == 'DELETE':
        output = delete_from_aws(BUCKET, filename)
        return "Deleted"


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=80)
