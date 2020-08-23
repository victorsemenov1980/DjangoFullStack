#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:11:53 2020

@author: user
"""



from django.template.defaulttags import register




@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)