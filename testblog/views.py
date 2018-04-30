# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from testblog.models import testblog_post, Category, Comment
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def home(req):
    testblog_list = testblog_post.objects.all()
    return render(req, 'home.html', {'testblog_list': testblog_list})

def get_category(req, category_name):
    find_category = Category.objects.get(name=category_name)
    postlist = find_category.testblog_post_set.all()
    return render(req, 'post.html', {'post_list': postlist})

def get_post_byname(req, post_name):
    find_post = testblog_post.objects.get(title=post_name)
    if req.POST:
        if req.user.is_authenticated:
            username = str(req.user.username)
            content = str(req.POST['content'])
            comment = Comment.objects.create(username=username, content=content, post=find_post)
            comment.save()
    comment_list = Comment.objects.filter(post=find_post)
    return render(req, 'post_byname.html', {'post': find_post, 'comment_list':comment_list})

def about(req):
    return render(req, 'about.html')

def get_post(req):
    find_post = testblog_post.objects.all()
    return render(req, 'post.html', {'post_list':find_post, 'comment_list':comment_list})

def signup(req):
    if req.POST:
        username = req.POST['username']
        password = req.POST['password']
        user = User.objects.create_user(username=str(username), password=str(password))
        user.save()
        return HttpResponseRedirect('/home')
    else:
        return render(req, 'signup.html')

def signin(req):
    if req.POST:
        if req.POST.has_key('signin'):
            username = req.POST['username']
            password = req.POST['password']
            user = authenticate(req, username=str(username), password=str(password))
            if user is not None:
                login(req, user)
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse('error')
        else:
            logout(req)
    return render(req, 'signin.html')


