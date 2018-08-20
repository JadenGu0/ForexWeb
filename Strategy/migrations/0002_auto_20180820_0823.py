# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-20 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strategy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='status',
            field=models.CharField(choices=[('INITIAL', 'INITIAL'), ('SAVED', 'SAVED'), ('PROCESSING', 'PROCESSING'), ('TESTED', 'TESTED')], default='INITIAL', max_length=50),
        ),
    ]
