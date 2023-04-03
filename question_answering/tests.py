from django.test import TestCase
from django.contrib.auth import get_user_model
from chatbot_management.models import Chatbot
from .models import Conversation
from .utils import fetch_answer_from_gpt3

User = get_user_model()


class QuestionAnsweringTestCase(TestCase):
    """
    Question answering test case.
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

    def test_fetch_answer_from_gpt3(self):
        """
        Test fetching an answer from GPT-3.
        """
        question = "What is the capital of France?"
        context = "The capital of France is Paris."
        answer = fetch_answer_from_gpt3(question, context)
        self.assertEqual(answer,
                         "Sample answer for question 'What is the capital of France?' in context 'The capital of France is Paris.'")

    def tearDown(self):
        """
        Clean up the test case.
        """
        self.user.delete()
        self.chatbot.delete()

