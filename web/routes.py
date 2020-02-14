from werkzeug.utils import secure_filename

from web import app
from flask import render_template, request
from web.templates.functions import allowed_file
import os


@app.route("/")
def home():
    return render_template('index.html', title='Home')


@app.route("/upload", methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
    return render_template("upload.html", title='Upload', filenames=filenames)

