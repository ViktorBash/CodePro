from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
# This is a signal that gets fired after an object is saved
# We will create a sender and reciever

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
"""
This 1st function recieves a signal/reciever, it then sends a signal
Kwargs just accepts any additional keyword arguments (which we won't be using)

Basically, this script makes it so when a user is created, a profile is made
for them.
"""
