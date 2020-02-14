from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, Separator, View, Link, Text
from os.path import join, dirname, realpath
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
nav = Nav(app)



@nav.navigation()
def mynavbar():
    return Navbar(
        'Graphit',
        View('Home', 'home'),
        View('Upload', 'upload')
    )


app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static/uploads/')
app.config['ALLOWED_EXTENSIONS'] = set(['gml', 'txt'])
app.config['SECRET_KEY'] = 'd22068be55575b2dabd7f45817036a97bd499d81fb8e4098'

from web import routes
