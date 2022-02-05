from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(CustomUser, self).save(*args, **kwargs)

    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)
    
    def __str__(self):
        return self.username