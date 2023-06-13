import unittest
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from your_module import RegistrationForm, LoginForm, RecipeForm, ProfileUpdateForm

class FormTest(unittest.TestCase):
    def test_registration_form(self):
        form = RegistrationForm()
        self.assertIsInstance(form.name, StringField)
        self.assertIsInstance(form.email, StringField)
        self.assertIsInstance(form.password, PasswordField)
        self.assertIsInstance(form.confirm_password, PasswordField)
        self.assertEqual(form.name.validators, [DataRequired()])
        self.assertEqual(form.email.validators, [DataRequired(), Email()])
        self.assertEqual(form.password.validators, [DataRequired(), Length(min=6)])
        self.assertEqual(form.confirm_password.validators, [EqualTo('password', message='Passwords must match')])

    def test_login_form(self):
        form = LoginForm()
        self.assertIsInstance(form.email, StringField)
        self.assertIsInstance(form.password, PasswordField)
        self.assertEqual(form.email.validators, [DataRequired(), Email()])
        self.assertEqual(form.password.validators, [DataRequired()])

    def test_recipe_form(self):
        form = RecipeForm()
        self.assertIsInstance(form.name, StringField)
        self.assertIsInstance(form.ingredients, StringField)
        self.assertIsInstance(form.directions, StringField)
        self.assertEqual(form.name.validators, [DataRequired()])
        self.assertEqual(form.ingredients.validators, [DataRequired()])
        self.assertEqual(form.directions.validators, [DataRequired()])

    def test_profile_update_form(self):
        form = ProfileUpdateForm()
        self.assertIsInstance(form.name, StringField)
        self.assertIsInstance(form.email, StringField)
        self.assertEqual(form.name.validators, [DataRequired()])
        self.assertEqual(form.email.validators, [DataRequired(), Email()])

if __name__ == '__main__':
    unittest.main()
