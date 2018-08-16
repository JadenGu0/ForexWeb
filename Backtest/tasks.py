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
    print info
    new_backtest=BackTest(info=info,strategy=strategy)
    new_backtest.save()
    strategy.status='TESTED'
    strategy.save()