from celery import Celery
import os
import sys
import django
pathname=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,pathname)
sys.path.insert(0,os.path.abspath(os.path.join(pathname,'..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ForexWeb.settings')
django.setup()
from Strategy.models import Strategy
from Backtest.models import BackTest
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def  backtest_start(strategy_id):
    strategy=Strategy.objects.get(pk=strategy_id)
    code=strategy.code
    filename=strategy.title+'.py'
    f=open(filename,'wb')
    f.write(code)
    f.close()
    commond1='import %s' %(strategy.title)
    exec(commond1)
    info=[]
    commond2='info =%s.main()' %(strategy.title)
    exec(commond2)
    new_backtest=BackTest(strategy=strategy,Profit=info[0][1],Sharp=info[1][1],MaxDrawdown=info[2][1],Buynumber=info[3][1],Buyprofit=info[4][1],Sellnumber=info[5][1]\
                          ,Sellprofit=info[6][1],Winrate=info[7][1],Profitfactor=info[8][1],Std=info[9][1],Mean=info[10][1])
    new_backtest.save()
    strategy.status='TESTED'
    strategy.save()