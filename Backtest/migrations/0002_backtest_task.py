# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-21 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backtest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backtest',
            name='task',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
