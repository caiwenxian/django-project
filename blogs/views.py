# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.db import connection
import logging; logging.basicConfig(level=logging.INFO)
import json
from .models import *
from .model.result import Result


# Create your views here.

#主页
def index(request):
    return render(request, 'blogs/index.html')

#登录
def login_view(request):
    username = 'admin'
    password = '3344'
    user = authenticate(request, username=username, password=password)
    if user is None:
        logging.info('user is not exit')
    else:
        logging.info('user is exit')
        login(request, user)
        result = {
            'code': 0,
            'msg': 'login success'
        }
        return HttpResponse(json.dumps(result), content_type="application/json")

#退出登录
def logout_view(request):
    logout(request)
    result = {
        'code': 0,
        'msg': 'logout success'
    }
    return HttpResponse(json.dumps(result), content_type="application/json")

#404界面
def not_found_page(request):
    return render(request, 'blogs/404.html')

#文章列表页面
# @login_required(login_url='/blogs/404')
def article_list_page(request):

    articles = Article.objects.all();
    logging.info(articles.query)
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    numberStr = [i for i in range(1, contacts.paginator.num_pages + 1)]
    if len(numberStr) > 3 and (contacts.number == 1 or contacts.number == 2):
        numberStr = numberStr[0:3]
        numberStr.append('...')
        numberStr.append(contacts.paginator.num_pages)
    elif len(numberStr) > 3 and (contacts.paginator.num_pages - contacts.number > 1):
        numberStr = numberStr[contacts.number - 1:contacts.number + 1]
        numberStr.append('...')
        numberStr.append(contacts.paginator.num_pages)
    else:
        numberStr = numberStr[contacts.paginator.num_pages - 3:contacts.paginator.num_pages]
    contacts.numberStr = numberStr
    return render(request, 'blogs/article_list.html', {'contacts': contacts})

#文章详细页面
def article_details_page(request, article_id):

    article = Article.objects.get(pk=article_id);
    # logging.info(articles.query)
    # paginator = Paginator(articles, 2)
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    result = Result(code=0, msg='success', data=article)
    return render(request, 'blogs/article_details.html', {'contacts': result})

#test
def test(request):
    articles = Article.objects.all();
    logging.info(articles.query)
    paginator = Paginator(articles, 2)
    page = int(request.GET.get('page'))
    contacts = paginator.get_page(page)
    return HttpResponse((articles), content_type="application/json")
    # return render(request, 'blogs/test.html')
