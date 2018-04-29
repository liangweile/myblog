# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class testblog_post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    category = models.ForeignKey(Category, default='')

    def __str__(self):
        return self.title



