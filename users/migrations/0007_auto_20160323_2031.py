# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-23 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160323_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='feed.Status'),
        ),
    ]
