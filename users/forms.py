from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
import email_validator
from users.models import User

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(name=username_to_check.data).first()
        if user:
            raise ValidationError("User already exists!")
    def validate_email(self,email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("E-mail already exists!")

    name=StringField(label="Full Name",validators=[Length(min=2,max=30),DataRequired()])
    email=StringField(label="E-mail",validators=[Email(),DataRequired()])
    password1=PasswordField(label="Create Password",validators=[Length(min=6,max=25),DataRequired()])
    password2=PasswordField(label="Confirm Password",validators=[EqualTo("password1"),DataRequired()])
    submit=SubmitField(label="Sign Up")

class LoginForm(FlaskForm):
    email = StringField(label='Registered E-mail:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')



