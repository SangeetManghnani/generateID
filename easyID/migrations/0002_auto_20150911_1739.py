# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyID', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
