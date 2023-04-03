from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class AuthenticationTestCase(TestCase):
    """
    Authentication test case.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        """
        Test the user creation.
        """
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_user_profile_creation(self):
        """
        Test the user profile creation.
        """
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertIsNotNone(user_profile)

    def tearDown(self):
        """
        Clean up the test case.
        """
        self.user.delete()
