from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from social_django.models import UserSocialAuth


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    subscription_type = models.CharField(max_length=10, choices=(('free', 'Free'), ('paid', 'Paid')), default='free')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserSocialAuth)
def update_user_profile_with_google_id(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        google_id = instance.uid
        user_profile = user.userprofile
        user_profile.google_id = google_id
        user_profile.save()
