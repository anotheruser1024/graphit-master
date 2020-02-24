
from web import app
from flask import render_template, redirect, session,url_for
from flask_uploads import configure_uploads, UploadSet, send_from_directory
from web.forms import UploadFile
import json as json


from networkx.exception import NetworkXError
# imports will be needed later
# import requests
from os.path import join, dirname, realpath
import os
import networkx as nx
# from networkx import NetworkXError as NetworkXError
# from datetime import datetime

graph = UploadSet('graph', app.config['ALLOWED_EXTENSIONS']) # configures flask file uploads likes to allowed extention env variable
configure_uploads(app, graph)  # instantiates file upload object


@app.route("/",  methods=['GET', 'POST'])
def home():
    # gets class objects with form
    form = UploadFile()

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
    #graph = 'static/uploads/graph/dolphins.gml'
    #files ="static\\uploads\\graph", 'dolphins.gml'
    #file =  os.path.join(app.config['UPLOADS_DEFAULT_DEST'] + 'graph' + '/dolphins.gml')
    #print(os.path.isfile(file))
    #file = nx.read_gml(file)
    #file = nx.node_link_data(file)
    #file = json.dumps(file)

    #print(type(file))

    #{url_for('static', filename='uploads/graph/karate.json')}}
    return render_template("upload.html", title='Upload', data='data')
