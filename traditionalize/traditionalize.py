#!/usr/bin/env python
#-*- coding: utf-8 -*-

#下載以下兩個文件
#zh_wiki.py:https://github.com/skydark/nstools/blob/master/zhtools/zh_wiki.py
#langconv.py:https://github.com/skydark/nstools/blob/master/zhtools/langconv.py

from langconv import Converter

line = u"籃球"
print line

line = Converter('zh-hans').convert(line)
print type(line), line
