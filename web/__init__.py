from flask import Flask, session
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask(__name__)
app.config.from_object('config.Development')
bootstrap = Bootstrap(app)
nav = Nav(app)




@nav.navigation()
def mynavbar():

    if 'filename' not in session:
        return Navbar(

            'Graphit',
            View('Home', 'home'),
            View('Upload', 'upload')

        )
    else:
         return Navbar(

        'Graphit',
        View('Home', 'home'),
        View('Upload', 'upload'),
        View('filename', 'home')
        )


from web import routes
