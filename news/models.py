from django.db import models


class News(models.Model):
    date = models.DateField()
    posted_hour = models.TimeField()
    title = models.TextField()
    body = models.TextField()

    def __unicode__(self):
        return self.title