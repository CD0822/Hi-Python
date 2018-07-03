#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename: ex2_get_a_webpage.py
# History: July 3,2018 - [Dan Chen] created
# This file is written for a very simple method to get a website page from the url.

from urllib import request,error


url = "http://www.baidu.com"
try:
    request = request.urlopen(url)
    print("geturl: ", request.geturl())
    result = request.read().decode("utf-8")
    print(result)
except error.URLError as e:
    if hasattr(e, 'code'):
        print("HTTPError")
        print("status code is ",e.code)
    elif hasattr(e,'reason'):
        print("URLError")
        print("reason is ", e.reason)

