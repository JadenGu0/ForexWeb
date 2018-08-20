# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Strategy.models import Strategy
# Create your models here.

class BackTest(models.Model):
    strategy = models.ForeignKey(Strategy)
    profit=models.CharField(max_length=100,null=True)
    maxdrawdown = models.CharField(max_length=100, null=True)
    sharp = models.CharField(max_length=100, null=True)
    profitfactor = models.CharField(max_length=100, null=True)
    winrate = models.CharField(max_length=100, null=True)
    std = models.CharField(max_length=100, null=True)
    mean = models.CharField(max_length=100, null=True)
    buynumber = models.CharField(max_length=100, null=True)
    buyprofit = models.CharField(max_length=100, null=True)
    sellnumber = models.CharField(max_length=100, null=True)
    sellprofit = models.CharField(max_length=100, null=True)
