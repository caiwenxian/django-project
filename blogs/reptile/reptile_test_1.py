# -*- coding: UTF-8 -*-

from urllib import request
import chardet
import unittest
import logging; logging.basicConfig(level=logging.INFO)
from django.test import TestCase
import unittest
import json

def test1():
    response = request.urlopen('http://fanyi.baidu.com')
    html = response.read();
    # html = html.decode('utf-8')
    # logging.info(html)
    logging.info(chardet.detect(html))
    print("geturl打印信息：%s" % (response.geturl()))
    print('**********************************************')
    print("info打印信息：%s" % (response.info()))
    print('**********************************************')
    print("getcode打印信息：%s" % (response.getcode()))

def test2():
    request_url = 'https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=0&tsel=0&kc=0&tk=998691.637603&q=%E7%88%AC%E8%99%AB'
    kv = {
        ':authority': 'translate.google.cn',
        'referer': 'https://translate.google.cn/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'x-client-data': 'CJC2yQEIpbbJAQjEtskBCKmdygEIuZ3KAQien8oBCKijygE='
    }
    req = request.Request(request_url)
    req.add_header('referer', 'https://translate.google.cn/')
    req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    req.add_header('x-client-data', 'CJC2yQEIpbbJAQjEtskBCKmdygEIuZ3KAQien8oBCKijygE=')
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    result = json.loads(html)
    result = result[1][0][1][0]
    logging.info('result:%s' % result)

def test3():
    request_url = 'https://tool.lu/ip/'
    proxy = {'http': '116.77.204.2:80'}
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)
    req = request.Request(request_url)
    req.add_header('referer', 'https://translate.google.cn/')
    req.add_header('user-agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    req.add_header('x-client-data', 'CJC2yQEIpbbJAQjEtskBCKmdygEIuZ3KAQien8oBCKijygE=')
    response = request.urlopen(req)
    html = response.read().decode('utf-8')

    logging.info('html:%s' % html)

if __name__ == "__main__":
    # test1()
    #test2()
    test3()





