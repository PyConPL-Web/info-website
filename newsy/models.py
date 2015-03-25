from django.db import models


class News(models.Model):
    date = models.DateField()
    author = models.TextField()
    title = models.TextField()
    body = models.TextField()