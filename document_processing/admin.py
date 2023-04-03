from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    """
    Document admin class.
    """
    list_display = ('id', 'user', 'source_type', 'content', 'pinecone_index_id')
    list_filter = ('source_type',)
    search_fields = ('user__username', 'pinecone_index_id')


admin.site.register(Document, DocumentAdmin)
