# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0002_auto_20150911_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
