# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 08:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171023_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='type',
        ),
    ]
