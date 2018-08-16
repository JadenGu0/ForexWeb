# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from tasks import backtest_start
from models import BackTest
from Strategy.models import Strategy


# Create your views here.



def run(request,pk):
    print pk
    backtest_start.delay(pk)
    strategy=Strategy.objects.get(pk=pk)
    strategy.status='PROCESSING'
    strategy.save()
    return HttpResponseRedirect('/strategy/all/')