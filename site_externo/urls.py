# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
#from avaliacao import views
from . import views

urlpatterns = patterns(views,    
    url('^$', views.index, name='home'),
)