# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testblog.models import testblog_post, Category, Comment

# Register your models here.

class testblog_admin(admin.ModelAdmin):
    list_display = ['title', 'body']

class category_admin(admin.ModelAdmin):
    list_display = ['name']

class comment_admin(admin.ModelAdmin):
    list_display = ['username', 'content']

admin.site.register(testblog_post, testblog_admin)
admin.site.register(Category, category_admin)
admin.site.register(Comment, comment_admin)

