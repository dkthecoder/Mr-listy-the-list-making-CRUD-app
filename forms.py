from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')

class MyAccountForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=2, max=50)])
    email = StringField('Email', validators=[Email()])
    old_password = PasswordField('Old Password')
    password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm New Password', validators=[EqualTo('password')])
    submit = SubmitField('Make Change')

class ListForm(FlaskForm):
    list_item = TextAreaField('Note', validators=[DataRequired()])
    mark_done = BooleanField('Mark Done?!')
    submit = SubmitField('Add')

class NewListForm(FlaskForm):
    new_list_name = StringField('List name', validators=[Length(min=2, max=50)])
    new_list_description = TextAreaField('List Description', validators=[DataRequired()])
    submit = SubmitField('Make New List')