# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import Strategy
from forms import StrategyForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_strategy(request):
    if request.method == 'GET':
        return render(request, 'Strategy/add.html')
    if request.method == 'POST':
        title=request.POST['Title']
        desc=request.POST['Description']
        code=request.POST['Code']
        strategy=Strategy(title=title,user=request.user,description=desc,code=code,status='INITIAL')
        strategy.save()
        strategys = Strategy.objects.filter(user=request.user)
        return render(request, 'Strategy/index.html', {'strategy': strategys})


@login_required
def strategy_detail(requset, pk):
    strategy = Strategy.objects.get(pk=pk)
    ins = StrategyForm(instance=strategy)
    return render(requset, 'Strategy/detail.html', {'strategy': ins})


@login_required
def strategy_index(request):
    strategys = Strategy.objects.filter(user=request.user)
    return render(request, 'Strategy/index.html', {'strategy': strategys})

@login_required
def delete(request,pk):
    strategy=Strategy.objects.get(pk=pk)
    strategy.delete()
    strategys = Strategy.objects.filter(user=request.user)
    return render(request, 'Strategy/index.html', {'strategy': strategys})

@login_required
def detail(request,pk):
    strategy=Strategy.objects.get(pk=pk)
    form=StrategyForm(instance=strategy)
    return render(request,'Strategy/detail.html',{'strategy':form})