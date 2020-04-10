from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
# cascade means if the user is deleted, the profile will be deleted, but if
# The profile is deleted, the user is not deleted
"""
For image, default= is what the default image of a user will be.
upload_to= is where the images will be uploaded (the directory)
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about_info = models.TextField(default="Hi! I am a fellow Python programmer.")

    # Whenever the profile is printed, it will print out the username
    def __str__(self):
        return f'{self.user.username}'

    # Overriding save method to cut down photo size
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
