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
        obj = StrategyForm()
        return render(request, 'Strategy/add.html', {'obj': obj})
    if request.method == 'POST':
        obj = StrategyForm(request.POST)
        if obj.is_valid():
            obj.save()
        return HttpResponseRedirect('/strategy/all/')


@login_required
def strategy_detail(requset, pk):
    strategy = Strategy.objects.get(pk=pk)
    ins = StrategyForm(instance=strategy)
    return render(requset, 'Strategy/detail.html', {'strategy': ins})


@login_required
def strategy_index(request):
    strategys = Strategy.objects.filter(user=request.user)
    return render(request, 'Strategy/index.html', {'strategy': strategys})
