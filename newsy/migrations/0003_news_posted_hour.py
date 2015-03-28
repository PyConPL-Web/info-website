# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsy', '0002_remove_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='posted_hour',
            field=models.TimeField(default=datetime.datetime(2015, 3, 28, 8, 55, 16, 652622, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
