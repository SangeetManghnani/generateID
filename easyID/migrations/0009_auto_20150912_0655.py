# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0008_auto_20150912_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 6, 55, 57, 133675, tzinfo=utc)),
        ),
    ]
