# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 10:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160404_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doubantopic',
            name='image_url',
        ),
    ]
