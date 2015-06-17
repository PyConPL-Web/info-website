# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20150326_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 11, 24, 44, 443000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
