from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Document model serializer.
    """

    class Meta:
        model = Document
        fields = ['id', 'user', 'document_type', 'content', 'pinecone_index_id']
