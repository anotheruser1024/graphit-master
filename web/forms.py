from web import app
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MyUploadFile(FlaskForm):
    choosefile = FileField(u'Choose File', validators=[FileRequired(),
                                                      FileAllowed(app.config['ALLOWED_EXTENSIONS'], message='Not Valid Graph file')])

    submit = SubmitField('Upload File')

