from django.db import models


class Event(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    desc = models.TextField()
    title = models.CharField(max_length=150)
    prelector = models.CharField(max_length=50)
    classroom = models.CharField(max_length=3)
    type = models.ForeignKey('Type', null=True, blank=True)

    def __unicode__(self):
        return "{title}".format(title=self.title)

    def __str__(self):
        return unicode(self)


class Type(models.Model):
    pass
