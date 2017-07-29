import os
from flask import Flask, request, redirect, url_for, render_template, send_file, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            response = jsonify(message='No file part')
            response.status_code = 422
            return response
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            response = jsonify(message='Empty filename')
            response.status_code = 422
            return response
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(message='success')
    return render_template('index.html')

@app.route('/obj', methods=['GET'])
def serve_obj():
    return send_file('static/cube.obj', as_attachment=True, attachment_filename='response.obj')
