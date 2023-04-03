from rest_framework import serializers
from .models import Chatbot


class ChatbotSerializer(serializers.ModelSerializer):
    """
    Chatbot serializer for the Chatbot model.
    """

    class Meta:
        model = Chatbot
        fields = ['id', 'user', 'name', 'created_at', 'updated_at']
