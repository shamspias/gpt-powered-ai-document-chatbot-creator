from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    """
    Document model representing an uploaded document (PDF, DOC, or URL).
    """
    CHOICES = [
        ("PDF", "PDF"),
        ("DOCX", "DOCX"),
        ("CSV", "CSV"),
        ("XLS", "XLS"),
        ("PPTX", "PPTX"),
        ("IMAGE", "IMAGE"),
        ("URL", "URL"),
        ("WEBSITE", "WEBSITE"),
        ("YOUTUBE", "YOUTUBE"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=10,
                                   choices=CHOICES)
    content = models.TextField()
    pinecone_index_id = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.source_type} ({self.pinecone_index_id})'
