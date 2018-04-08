from flask_wtf import FlaskForm
from wtforms import StringField, TextField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
class MyForm(FlaskForm):
 name = StringField('name', validators=[DataRequired()])
 email = StringField('email', validators=[Email()])
 subject = TextField('subject', validators=[DataRequired()])
 message = TextAreaField('message', validators=[DataRequired()])
 submit = SubmitField("Send")