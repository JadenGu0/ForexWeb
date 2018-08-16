# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Strategy.models import Strategy
# Create your models here.

class BackTest(models.Model):
    strategy = models.ForeignKey(Strategy)
    info = models.CharField(max_length=500)