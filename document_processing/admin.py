from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Document model admin configuration.
    """
    list_display = ('user', 'document_type', 'pinecone_index_id')
    search_fields = ('user__username', 'document_type', 'pinecone_index_id')
