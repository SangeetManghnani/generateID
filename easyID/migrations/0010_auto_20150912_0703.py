# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0009_auto_20150912_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 9, 12, 7, 3, 47, 135622, tzinfo=utc)),
        ),
    ]
