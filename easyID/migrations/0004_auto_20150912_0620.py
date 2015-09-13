# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0003_information_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 6, 20, 18, 550713), blank=True),
        ),
    ]
