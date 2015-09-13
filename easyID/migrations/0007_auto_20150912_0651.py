# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0006_information_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
