from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    """
    Document model representing an uploaded document (PDF, DOC, or URL).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)
    content = models.TextField()
    pinecone_index_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.document_type} ({self.pinecone_index_id})'
