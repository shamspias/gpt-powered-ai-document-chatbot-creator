from django.contrib import admin
from .models import Chatbot


@admin.register(Chatbot)
class ChatbotAdmin(admin.ModelAdmin):
    """
    ChatbotAdmin defines the admin interface for the Chatbot model.
    """
    list_display = ('id', 'user', 'name', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('name',)
    ordering = ('-created_at',)
