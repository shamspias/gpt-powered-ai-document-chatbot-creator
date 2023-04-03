from django.db import models
from django.contrib.auth.models import User
from chatbot_management.models import Chatbot


class Conversation(models.Model):
    """
    Conversation model representing a chatbot conversation.
    """
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.chatbot.name}"
