# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
import logging
jieba.setLogLevel(60)
from RKT_class import RKT
import train as sw

# 原始文本
SourceText = "類似於PageRank的思想，將文本中的語法單元視作圖中的節點，如果兩個語法單元存在一定語法關係（例如共現），則這兩個語法單元在圖中就會有一條邊相互連接，通過一定的迭代次數，最終不同的節點會有不同的權重，權重高的語法單元可以作為關鍵詞。"

seg_list = jieba.lcut(SourceText,cut_all=False)


seg_list = sw.filter(seg_list)



a = RKT(seg_list,20)
print "\nTheta , keywords by textrank:"
#for i in a.Text_Array:print i
#for i in a.Text_Node_value:print i
#for i in a.TopText:print i,a.Text_Node[i],a.Text_Node_value[i]
for i in a.TopText_H2L:print (a.Text_Node[i]).encode('utf-8')+'/',

from jieba import analyse
# 引入TextRank关键词抽取接口
textrank = analyse.textrank
print "\njieba , keywords by textrank:"
# 基于TextRank算法进行关键词抽取
keywords = textrank(','.join(seg_list))
# 输出抽取出的关键词
for keyword in keywords:
    print keyword + "/",


# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags

# 基于TF-IDF算法进行关键词抽取
keywords = tfidf(','.join(seg_list))
print "\njieba , keywords by tfidf:"
# 输出抽取出的关键词
for keyword in keywords:
    print keyword + "/",

