# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:17:38 2022

@author: user
"""

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),'current_category': current_category}