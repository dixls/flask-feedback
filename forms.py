from click import password_option
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class Registration(FlaskForm):
    """Form for registering new users"""

    username
    password
    email
    first_name
    last_name