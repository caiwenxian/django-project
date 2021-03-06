#!/usr/bin/python
#coding:utf-8

from django.db import models
from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser


# Create your models here.
#文章实体
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    author_id = models.CharField(max_length=50)
    status = models.BooleanField()
    type = models.IntegerField('类型')
    browse_amount = models.IntegerField('浏览数')
    comment_amount = models.IntegerField('评论数')
    create_date = models.DateTimeField('create date')
    modify_date = models.DateTimeField('modify date')

class User(AbstractUser):
    """
    用户信息
    """
    photo_path = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta():
        db_table = 'user'






