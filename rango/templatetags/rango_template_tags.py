#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/29 3:59 上午
# @Author : mzt
# @Site : 
# @File : rango_template_tags.py.py
# @Software: PyCharm

from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/categories.html')
def get_category_list():
    return {'categories': Category.objects.all()}
