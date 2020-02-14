from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, Separator, View, Link, Text
from os.path import join, dirname, realpath
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
nav = Nav(app)
app.config.from_object('config.Development')


@nav.navigation()
def mynavbar():
    return Navbar(
        'Graphit',
        View('Home', 'home'),
        View('Upload', 'upload')
    )




from web import routes
