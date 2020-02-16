
from web import app
from flask import render_template, request, redirect, session
from flask_uploads import configure_uploads, UploadSet
from web.forms import MyUploadFile
import os
from datetime import datetime

graph = UploadSet('graph', app.config['ALLOWED_EXTENSIONS'])
configure_uploads(app, graph)

@app.route("/",  methods=['GET', 'POST'])
def home():
    form = MyUploadFile()

    if form.validate_on_submit():

        filename = graph.save(form.choosefile.data)
        print(filename)
        if filename not in session:
            session["filename"] = []
            session["filename"].append(filename)
        else:
            session["filename"].append(filename)



        return redirect('/upload')

    return render_template('index.html', title='Home', form=form)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if "filename" in session:
        files = session["filename"]
    return render_template("upload.html", title='Upload', files='files')
