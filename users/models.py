from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PyconUser(models.Model):
    username = models.TextField(unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    is_confirmed = models.BooleanField(default=False)
    confirm_string = models.TextField()

    def __str__(self):
        return self.username + ' ' + self.email + str(self.is_confirmed)