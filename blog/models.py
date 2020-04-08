from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Reverse returns the string of the url
    # This is used to redirect user to the post they made when making a new
    # post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
