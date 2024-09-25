from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import SignUp, LoginAction

# Signal to track user sign-up
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
      if created:
            SignUp.objects.create(user=instance)

# Signal to track user login
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
      LoginAction.objects.create(user=user)
