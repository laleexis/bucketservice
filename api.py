from flask import Flask, request
from defs import upload_to_aws, get_all_s3_keys, download_from_aws, delete_from_aws

app = Flask(__name__)
UPLOAD_FOLDER = "."
BUCKET = "supportmeli"
path = "C:/Users/alucero/Documents"


@app.route('/')
def entry_point():
    return 'Test API'


@app.route("/files", methods=['GET'])  # json in body
def storage():
    req_data = request.get_json()
    if request.method == "GET":
        contents = get_all_s3_keys(req_data['BUCKET'], req_data['ACCESS_KEY'], req_data['SECRET_KEY'])
        print(req_data['BUCKET'])
        return contents


@app.route("/files/<filename>", methods=['POST'])
def upload(filename):
    req_data = request.get_json()
    if request.method == "POST":
        r=upload_to_aws(req_data['LOCAL_PATH']+str(filename), req_data['BUCKET'], filename, req_data['ACCESS_KEY'],
                      req_data['SECRET_KEY'])
        return r


@app.route("/files/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        req_data = request.get_json()
        download_from_aws(filename, req_data["BUCKET"], req_data["ACCESS_KEY"], req_data["SECRET_KEY"])
        return "Downloaded to instance"


@app.route("/files/<filename>", methods=['DELETE'])
def delete(filename):
    if request.method == 'DELETE':
        delete_from_aws(BUCKET, filename)
        return "Deleted"


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=80)
