import unittest
from flask import Flask
from wtforms.validators import ValidationError
from app.forms import RegistrationForm, LoginForm, RecipeForm, ProfileUpdateForm

class FormTestCase(unittest.TestCase):
    def test_registration_form(self):
        form = RegistrationForm(name='John Doe', email='johndoe@example.com', password='password', confirm_password='password')
        self.assertTrue(form.validate())

    def test_registration_form_missing_data(self):
        form = RegistrationForm()
        self.assertFalse(form.validate())
        self.assertIn('Name is required', form.name.errors)
        self.assertIn('Email is required', form.email.errors)
        self.assertIn('Password is required', form.password.errors)

    def test_registration_form_invalid_email(self):
        form = RegistrationForm(email='invalid_email', password='password', confirm_password='password')
        self.assertFalse(form.validate())
        self.assertIn('Invalid email address', form.email.errors)

    def test_registration_form_password_mismatch(self):
        form = RegistrationForm(password='password', confirm_password='different_password')
        self.assertFalse(form.validate())
        self.assertIn('Passwords must match', form.confirm_password.errors)

    # Add more test cases for other forms as needed

if __name__ == '__main__':
    unittest.main()
