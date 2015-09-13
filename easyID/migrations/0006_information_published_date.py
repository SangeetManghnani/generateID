# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0005_remove_information_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 6, 22, 57, 94902, tzinfo=utc)),
        ),
    ]
