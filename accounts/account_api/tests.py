from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
# Create your tests here.
class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        data = {
            "user": {
                "username": "testuser",
                "email": "test@example.com",
                "password": "testpassword"
            }
        }
        response = self.client.post('/register/', data, format='json')
        self.assertEqual(response.status_code, 201)