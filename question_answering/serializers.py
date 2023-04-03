from rest_framework import serializers
from .models import Conversation


class ConversationSerializer(serializers.ModelSerializer):
    """
    Conversation serializer for the Conversation model.
    """

    class Meta:
        model = Conversation
        fields = ['id', 'chatbot', 'user', 'text', 'response', 'created_at']
