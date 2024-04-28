from django.test import TestCase 
from django.contrib.auth.models import User
from schedrule_app.forms import SignupForm


class SignupFormTests(TestCase):
    def test_signup_form_valid(self):
        """Test if the form is valid with valid data."""
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_passwords_not_matching(self):
        """Test if the form is invalid when passwords don't match."""
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword'
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_signup_form_invalid_username_taken(self):
        """Test if the form is invalid when username is already taken."""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='existingpassword123')
        form_data = {
            'username': 'existinguser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)