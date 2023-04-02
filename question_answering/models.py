from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    """
    A document uploaded by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    extracted_text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Embedding(models.Model):
    """
    A document embedding.
    """
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    vector = models.JSONField()

    def __str__(self):
        return f"Embedding for {self.document.title}"
