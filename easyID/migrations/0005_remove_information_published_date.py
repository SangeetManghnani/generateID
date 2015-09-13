# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0004_auto_20150912_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='published_date',
        ),
    ]
