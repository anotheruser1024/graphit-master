
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

graph = UploadSet('graph', app.config['ALLOWED_EXTENSIONS']) # configures flask file uploads likes to allowed extention env variable
configure_uploads(app, graph)  # instantiates file upload object


@app.route("/",  methods=['GET', 'POST'])
def home():
    # gets class objects with form
    form = MyUploadFile()

    if form.validate_on_submit(): #vaildats form

        filename = graph.save(form.choosefile.data) # see docs https://pypi.org/project/Flask-Uploads/
        print(filename) # prints file name to teminal
        if 'filename' not in session: # checks sessions for filename list
            session["filename"] = [] #assings list to sessions
            sessionList = session['filename']  # additional list need Bug in sessions can't append to list in sessions dict
            sessionList.append(filename)
            session['filename'] = sessionList # reassigns list to sessions

        else:
            sessionList = session["filename"]

            sessionList.append(filename)
            session['filename'] = sessionList

        return redirect('/upload') #redirect to uploads if task is done

    return render_template('index.html', title='Home', form=form) # renders template for page


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    files = session.get('filename')

    return render_template("upload.html", title='Upload', files='files')
