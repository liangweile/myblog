# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from testblog.models import testblog_post, Category
from django.shortcuts import render

# Create your views here.

def home(req):
    testblog_list = testblog_post.objects.all()
    return render(req, 'home.html', {'testblog_list': testblog_list})

def get_category(req, category_name):
    find_category = Category.objects.get(name=category_name)
    postlist = find_category.testblog_post_set.all()
    return render(req, 'home.html', {'testblog_list': postlist})

