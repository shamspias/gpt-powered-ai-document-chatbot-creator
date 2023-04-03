from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Chatbot

User = get_user_model()


class ChatbotManagementTestCase(TestCase):
    """
    Chatbot management test case.
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
        self.chatbot = Chatbot.objects.create(
            user=self.user,
            name='Test Chatbot'
        )

    def test_chatbot_creation(self):
        """
        Test the chatbot creation.
        """
        chatbot = Chatbot.objects.get(id=self.chatbot.id)
        self.assertEqual(chatbot.name, 'Test Chatbot')
        self.assertEqual(chatbot.user, self.user)

    def tearDown(self):
        """
        Clean up the test case.
        """
        self.user.delete()
        self.chatbot.delete()
