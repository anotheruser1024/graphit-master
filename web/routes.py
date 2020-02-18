
from web import app
from flask import render_template, redirect, session
from flask_uploads import configure_uploads, UploadSet
from web.forms import MyUploadFile
from networkx.exception import NetworkXError
# imports will be needed later
# import requests
# import os
# import networkx as nx
# from networkx import NetworkXError as NetworkXError
# from datetime import datetime

graph = UploadSet('graph', app.config['ALLOWED_EXTENSIONS'])
configure_uploads(app, graph)


@app.route("/",  methods=['GET', 'POST'])
def home():
    form = MyUploadFile()

    if form.validate_on_submit():

        filename = graph.save(form.choosefile.data)
        print(filename)
        if 'filename' not in session:
            session["filename"] = []
            sessionList = session['filename']
            sessionList.append(filename)
            session['filename'] = sessionList

        else:
            sessionList = session["filename"]

            sessionList.append(filename)
            session['filename'] = sessionList

        return redirect('/upload')

    return render_template('index.html', title='Home', form=form)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    files = session.get('filename')

    return render_template("upload.html", title='Upload', files='files')
