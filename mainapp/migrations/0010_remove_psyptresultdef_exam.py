# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20170430_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psyptresultdef',
            name='exam',
        ),
    ]
