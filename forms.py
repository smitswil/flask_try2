from flask.ext.wtf import Form
from wtforms import StringField,StringField, BooleanField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.validators import DataRequired
class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired(),validators.Email("Please enter a valid Email Address")])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [validators.DataRequired("Please enter a message.")])
    submit = SubmitField("Send")

