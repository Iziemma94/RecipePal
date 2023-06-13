from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[validators.EqualTo('password', message='Passwords must match')])

class LoginForm(Form):
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

class RecipeForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])
    ingredients = StringField('Ingredients', validators=[validators.DataRequired()])
    directions = StringField('Directions', validators=[validators.DataRequired()])

class ProfileUpdateForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
