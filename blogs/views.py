#!/usr/bin/python
#coding:utf-8

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
from bottle import *
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import uuid
from .utils.file_operate_util import FileOperateUtil
from configparser import ConfigParser
import datetime


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
            'status': 0,
            'msg': 'login success'
        }
        return HttpResponse(json.dumps(result), content_type="application/json")

#退出登录
def logout_view(request):
    logout(request)
    result = {
        'status': 0,
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
    elif len(numberStr) > 3 and (contacts.number > 2):
        numberStr = numberStr[0:1]
        numberStr.append("...")
        numberStr.append(contacts.number - 1)
        numberStr.append(contacts.number)
        numberStr.append(contacts.number + 1)
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
    result = Result(status=0, msg='success', data=article)
    return render(request, 'blogs/article_details.html', {'contacts': result})

#保存头像信息
def update_user_photo(request):
    form_data = request.POST
    photo_path = form_data.get('file_path')
    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(pk=current_user.id)
        user.photo_path = photo_path
        user.save()
    return HttpResponse(json.dumps(Result().__dict__), content_type="application/json")

#获取用户头像
def get_user_photo(request):
    photo_path = None
    if request.user.is_authenticated:
        photo_path = request.user.photo_path
    data = {
        'photo_path': photo_path
    }
    result = Result()
    result.data = data
    return HttpResponse(json.dumps(result.__dict__), content_type="application/json")

#上传图片
def upload_img(request):
    result = Result()
    #读取配置文件
    base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径
    config_path = base_path + '/config/config.ini'
    cfg = ConfigParser()
    cfg.read(config_path)
    upload_path = cfg.get('constant', 'FILE_PATH') # 上传文件目录
    # upload_path = os.path.join(base_path, 'upload')  # 上传文件目录

    if not os.path.exists(upload_path):
        os.makedirs(upload_path)

    if request.method == 'POST':
        file_obj = request.FILES.get("up_file")
        logging.info('开始上传文件：' + file_obj.name)
        arr = file_obj.name.split('.')
        name = arr[len(arr) - 1]
        ramdom_id = str(int(time.time()))
        file_name = ramdom_id + '.' + name
        nowTime = datetime.datetime.now()
        year = nowTime.strftime('%Y')
        #相对路径
        file_path = '/' + nowTime.strftime('%Y') + '/' + nowTime.strftime('%m') + '/' + nowTime.strftime('%d') + '/'
        #磁盘路径
        absolute_path = upload_path + file_path
        #判断路径是否存在，不存在则创建
        FileOperateUtil.validate_folder_exists(absolute_path, True)
        f1 = open(absolute_path + file_name, "wb")
        for i in file_obj.chunks():
            f1.write(i)
        f1.close()
        #返回相对路径即可
        data = {
            'file_name': file_name,
            'file_path': file_path + file_name
        }
        result.data = data
    else:
        form = UploadFileForm()
    return HttpResponse(json.dumps(result.__dict__), content_type="application/json")


#加载图片
def load_img(request):
    get_data = request.GET
    file_path = get_data.get('file_path')
    down_file_name = None
    base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径
    #加载配置文件
    config_path = base_path + '/config/config.ini'
    cfg = ConfigParser()
    cfg.read(config_path)
    upload_path = cfg.get('constant', 'FILE_PATH')  # 上传文件目录
    real_path = upload_path + file_path

    if os.path.exists(real_path):
        # 判断文件是否是文件
        if os.path.isfile(real_path):
            # 获取文件本身自己的名称
            filename = os.path.basename(real_path)
            # 若未指定下载文件名，则已文件本身名称为准
            if down_file_name is None:
                down_file_name = filename
            # 读取文件流，并构造请求响应
            response = HttpResponse(FileOperateUtil.file_iterator(real_path))
            # 设置响应流
            response['Content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename={0}'.format(
                down_file_name.encode('utf-8').decode('utf-8'))
        else:
            response = HttpResponse("下载失败,不是一个文件!", content_type="text/plain;charset=utf-8")
    else:
        response = HttpResponse("文件不存在,下载失败!", content_type="text/plain;charset=utf-8")
    return response


#test
def test(request):
    articles = Article.objects.all();
    logging.info(articles.query)
    paginator = Paginator(articles, 2)
    page = int(request.GET.get('page'))
    contacts = paginator.get_page(page)
    return HttpResponse((articles), content_type="application/json")
    # return render(request, 'blogs/test.html')
