from django.db import models

class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    desc = models.TextField(blank=True)
    title = models.CharField(max_length=150)
    prelector = models.CharField(max_length=50)
    classroom = models.CharField(max_length=3)
    type = models.ForeignKey('Type', null=True, blank=True)

    def __unicode__(self):
        return "{title}".format(title=self.title)

    def __str__(self):
        return unicode(self)

    def getStartTime(self):
        return self.start_time.hour + self.start_time.minute

    #def getEndTime(self):
     #   return self.end_time.hour + self.end_time.minute

class Type(models.Model):
    pass
