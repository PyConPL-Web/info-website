from django.db import models
from django.db.models import User as DUser


# based on pl.pycon.org/2015/ukarta,id 
class User(DUser):
    is_confirmed = models.BooleanField(default=False)  # user paid for entrance
    activation_string= models.CharField(max_length=32, default='')  # part of link to activate account
    hometown = models.CharField(max_length=50, default='')
    is_adult = models.BooleanField()
    patron_name = models.CharField(max_length=50, default='')

    def __repr__(self):
        return "User({})".format(self.username)
