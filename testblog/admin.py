# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testblog.models import testblog_post, Category

# Register your models here.

class testblog_admin(admin.ModelAdmin):
    list_display = ['title', 'body']

class category_admin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(testblog_post, testblog_admin)
admin.site.register(Category, category_admin)

