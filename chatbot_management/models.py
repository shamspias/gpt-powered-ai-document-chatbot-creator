from django.db import models
from django.contrib.auth.models import User


class Chatbot(models.Model):
    """
    Chatbot model representing a user's chatbot.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
