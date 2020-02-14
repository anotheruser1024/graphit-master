from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

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


from web.static.uploads import routes
