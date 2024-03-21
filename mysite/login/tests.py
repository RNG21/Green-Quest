from django.test import TestCase
from django.urls import reverse

from db.models import User

class RegisterViewTest(TestCase):
    def test_register_success(self):
        # Create a POST request with valid data
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com'
        })

        # Check that the user is redirected to the login page
        self.assertRedirects(response, '/login/')

        # Check that the user is created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_password_mismatch(self):
        # Create a POST request with mismatched passwords
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password': 'testpassword',
            'password2': 'differentpassword',
            'email': 'test@example.com'
        })

        # Check that the user is not created in the database
        self.assertFalse(User.objects.filter(username='testuser').exists())

        # Check that the error message is displayed in the response
        self.assertContains(response, 'The passwords entered do not match!')

    def test_register_empty_username(self):
        # Create a POST request with an empty username
        response = self.client.post(reverse('register'), {
            'username': '',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com'
        })

        # Check that the user is not created in the database
        self.assertFalse(User.objects.filter(username='').exists())

        # Check that the error message is displayed in the response
        self.assertContains(response, 'Username cannot be empty!')

    def test_register_existing_username(self):
        # Create a user with the same username in the database
        User.objects.create_user(username='existinguser', password='testpassword')

        # Create a POST request with an existing username
        response = self.client.post(reverse('register'), {
            'username': 'existinguser',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com'
        })

        # Check that there is only one user with username 'existinguser' in the database
        self.assertEqual(User.objects.filter(username='existinguser').count(), 1)

        # Check that the error message is displayed in the response
        self.assertContains(response, 'Username already exists. Please Choose a different one.')