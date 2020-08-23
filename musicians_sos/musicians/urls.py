#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:42:14 2020

@author: user
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('success', views.success,name='success'),
    path('nursing', views.nursing,name='nursing'),
    path('professional', views.professional,name='professional'),
    path('home', views.home,name='home'),
    path('wedding', views.wedding,name='wedding'),
    path('recording', views.recording,name='recording'),
    path('lessons', views.lessons,name='lessons'),
    path('faq', views.faq,name='faq'),
    path('manage', views.manage,name='manage'),
    path('manage_account', views.manage_account,name='manage_account'),
    path('add_service', views.add_service,name='add_service'),
    path('<int:account_id>', views.account,name='account'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)