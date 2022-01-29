# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 20:15:41 2022

@author: user
"""

from django.urls import path
from rango import views

app_name='rango'

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    ]
