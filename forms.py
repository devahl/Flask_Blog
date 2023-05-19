from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField ('Email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=)
