# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
import logging
jieba.setLogLevel(60)
from RKT_class import RKT
import Stop_word as sw

seg_list = jieba.lcut("happy「东森新闻」颠覆你对新闻的认知，改变你阅读新闻的习惯！在资讯爆炸的世代，让你的视野和国际接轨！ 「东森新闻」名列全球百大顶尖媒体，更是台湾最具代表性的新闻频道，经年累月声援民众倾诉，揭发不法陋习不遗余力，第一线的贴近采访，最深度权威的专题内容，除了东森新闻，只有「东森新闻」。",cut_all=False)

print seg_list
seg_list = sw.filter(seg_list)

print seg_list
'''
a = RKT(seg_list)
for i in a.Text_Node_value:print i
for i in a.TopText:print i,a.Text_Node[i],a.Text_Node_value[i]
'''
