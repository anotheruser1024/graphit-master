from os.path import join, dirname, realpath
from flask_uploads import configure_uploads

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'd22068be55575b2dabd7f45817036a97bd499d81fb8e4098'
    ALLOWED_EXTENSIONS = set(['gml', 'txt'])
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'web/static/uploads/')
    MAX_CONTENT_LENGTH = 0 * 1024 * 1024
    UPLOADED_FILES_DEST = join(dirname(realpath(__file__)), 'web/static/uploads/')
    UPLOADS_DEFAULT_DEST = 'web/static/uploads/'

class Production(Config):

    pass

class Development(Config):

    DEBUG = True
    TESTING = True
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

