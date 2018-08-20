from django.conf.urls import url,include
from django.contrib.auth.models import User
import views

urlpatterns=[

    url(r'^delete/(?P<pk>\d+)/$', views.delete),
    url(r'^detail/(?P<pk>\d+)/$', views.detail),
    url(r'^(?P<pk>\d+)/$',views.run),
    url(r'',views.backtest_index),
    #url(r'^all/',views.strategy_index)
]