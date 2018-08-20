# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from tasks import backtest_start
from models import BackTest
from Strategy.models import Strategy
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def run(request,pk):
    backtest_start.delay(pk)
    strategy=Strategy.objects.get(pk=pk)
    strategy.status='PROCESSING'
    strategy.save()
    return HttpResponseRedirect('/strategy/all/')

@login_required
def backtest_index(request):
    backtests=BackTest.objects.all()
    return render(request,'Backtest/index.html',{'index':backtests})

@login_required
def detail(request,pk):
    backtest=BackTest.objects.get(pk=pk)
    image='/home/jaden/Github/ForexWeb/static/img/'+backtest.strategy.title+'.png'
    return render(request,'Backtest/detail.html',{'image':image,'backtest':backtest})

@login_required
def delete(request,pk):
    backtest = BackTest.objects.get(pk=pk)
    str='rm /home/jaden/Github/ForexWeb/static/img/%s.png' %(backtest.strategy.title)
    exec(str)
    return render(request,'Backtest/index.html')