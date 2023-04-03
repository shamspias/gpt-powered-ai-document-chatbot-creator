from django.contrib import admin
from .models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """
    ConversationAdmin defines the admin interface for the Conversation model.
    """
    list_display = ('id', 'chatbot', 'user', 'text', 'response', 'created_at')
    list_filter = ('chatbot', 'user',)
    search_fields = ('text', 'response')
    ordering = ('-created_at',)