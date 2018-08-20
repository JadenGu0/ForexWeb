# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-20 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('code', models.TextField()),
                ('status', models.CharField(choices=[('INITIAL', 'INITIAL'), ('SAVED', 'SAVED'), ('PROCESSING', 'PROCESSING'), ('TESTED', 'TESTED')], default='INITIAL', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
