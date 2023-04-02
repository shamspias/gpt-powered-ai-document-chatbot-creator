from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    A user.
    """
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
