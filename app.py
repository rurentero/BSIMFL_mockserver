import os
from flask import Flask, request, Response, send_from_directory, send_file

# Fuente: https://roytuts.com/python-flask-file-upload-example/
# Si se ejecuta en Windows, para que el servidor sea visible es necesario ejecutar desde terminal
# con el siguiente comando: flask run --host=0.0.0.0

UPLOAD_FOLDER = 'C:/Users/usuario13/Documents/server_files'
HOST_IP = '192.168.1.38'
HOST_PORT = 5000

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return Response("No file part", status=400, mimetype='application/json')
        file = request.files['file']
        if file.filename == '':
            print('No file selected for uploading')
            return Response("No file selected for uploading", status=400, mimetype='application/json')
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('File successfully uploaded')
            return Response("File successfully uploaded", status=200, mimetype='application/json')
        else:
            print('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return Response("Server error", status=400, mimetype='application/json')


@app.route('/global', methods=['GET'])
def get_global_model():
    if request.method == 'GET':
        filename = "model_global"
        # Returning file from appended path
        print('Sending file')
        #file_path = os.path.abspath(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        #return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename)
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename),
                         mimetype='application/octet-stream',
                         attachment_filename='Adjacency.csv',
                         as_attachment=True)


if __name__ == '__main__':
    app.run(host=HOST_IP, port=HOST_PORT)
