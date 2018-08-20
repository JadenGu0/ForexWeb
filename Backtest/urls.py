from django.conf.urls import url,include
from django.contrib.auth.models import User
import views

urlpatterns=[
    url(r'',views.backtest_index),
    url(r'^(?P<pk>\d+)/$',views.run),
    #url(r'^all/',views.strategy_index)
]