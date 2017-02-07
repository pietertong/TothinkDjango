# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from front.models import Article, Author, Tag


# Create your views page here.
# <!--
# 不带参数的：
# {% url 'name' %}
# 带参数的：参数可以是变量名
# {% url 'name' 参数 %}
# -->
def home (request) :
    return render ( request, 'front/home.html' )


def learnTemplate (request) :
    learnTemplate = u"我在学习Django Framework,By myself."
    TutorialList = [
        "Html", "Css", "Jquery", "Python", "Django"
    ]
    directoryList = {
        'site' : u'自学学堂',
        'content' : u'各种IT技术教程'
    }
    listMap = map ( str, range ( 20 ) )
    return render (
            request,
            'front/learn_template.html',
            {
                'learn_template' : learnTemplate,
                'code' : '{{code}}',
                'tutorial_list' : TutorialList,
                'tag' : '{%tag%}',
                'directory_list' : directoryList,
                'list_map' : listMap
            }
    )


def learnQueryset (request) :
    print str ( Author.objects.filter ( name = "pieter" ).query )
    print  (Author.objects.all ( ))
    authors = Author.objects.values_list ( 'name', 'qq' )
    authorsLists = list ( authors )
    return render (
        request,
        'front/learn_queryset.html',
        {
            'authors':authorsLists
        }
    )


# Create your views here.
def index (request) :
    return HttpResponse ( u"欢迎自学Python，Django FrameWork" )


# Create your views here. plues a ,b ,push view page
# /add/?a=1&b=3
def add (request) :
    a = request.GET.get ( 'a', 0 )
    b = request.GET.get ( 'b', 0 )
    c = int ( a ) + int ( b )
    return HttpResponse ( str ( c ) )


# Create your views here. plues a ,b ,push view page
# /addparams/2/4
def addparams (request, a = 0, b = 0) :
    c = int ( a ) + int ( b )
    return HttpResponse ( str ( c ) )


def oldAddRedirect (request, a = 0, b = 0) :
    return HttpResponseRedirect (
            reverse ( 'addparams', args = (a, b) )
    )
