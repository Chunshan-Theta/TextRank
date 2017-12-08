# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
import logging
jieba.setLogLevel(10)


#美國一名獨居男子經常光顧當地的披薩店而日前突然在家發病他萬萬沒有想到自己的救命恩人就是自己平常叫外送的披薩店店長
seg_list = jieba.cut("「东森新闻」颠覆你对新闻的认知，改变你阅读新闻的习惯！在资讯爆炸的世代，让你的视野和国际接轨！ 「东森新闻」名列全球百大顶尖媒体，更是台湾最具代表性的新闻频道，经年累月声援民众倾诉，揭发不法陋习不遗余力，第一线的贴近采访，最深度权威的专题内容，除了东森新闻，只有「东森新闻」。",cut_all=False)
#seg_list = jieba.cut("美國一名獨居男子經常光顧當地披薩店日前突然在家發病他萬萬沒有想到自己救命恩人就是自己平常叫外送披薩店店長",cut_all=True)
#seg_list = jieba.cut_for_search("美国一名独居男子经常光顾当地披萨店日前突然在家发病他万万没有想到自己救命恩人就是自己平常叫外送披萨店店长")
Text_Array =[]
Text_Node =[]
Text_Node_Connection = []
Get_Top_Num = 10
WindowsSize = 5
for i in seg_list:
    Text_Array.append(i)
print '/'.join(Text_Array)



for i in range(len(Text_Array)):
    if Text_Array[i] not in Text_Node:
        Text_Node.append(Text_Array[i])
    connect = []
    if i-WindowsSize<0:
        for j in range(0,i+WindowsSize+1):
            if i != j:
                try:
                    connect.append(Text_Array[j])
                except IndexError as e:
                    jieba.Write_Log_Debug("Debug IndexError: "+str(e)+", reducing windows size, please.")

    elif i+WindowsSize >= len(Text_Array):
        for j in range(i-WindowsSize,len(Text_Array)):
            if i != j:
                connect.append(Text_Array[j])

    else:
        for j in range(i-WindowsSize,i+WindowsSize+1):
            if i != j:
                connect.append(Text_Array[j])
    Text_Node_Connection.append([Text_Array[i],connect])
print '/'.join(Text_Node)



    

for i in range(len(Text_Node_Connection)):
    Text_Node_Connection[i][0] = Text_Node.index(Text_Node_Connection[i][0])
    for j in range(len(Text_Node_Connection[i][1])):
        Text_Node_Connection[i][1][j]=Text_Node.index(Text_Node_Connection[i][1][j])


Text_Node_Connection_weight = np.zeros((len(Text_Node), len(Text_Node)),int)
Text_Node_value = np.arange(float(len(Text_Node)))

for i in range(len(Text_Node_value)):
    Text_Node_value[i]=1
#print Text_Node_value

for i in Text_Node_Connection:
    for j in i[1]:
        row = int(i[0])
        col = int(j)
        Text_Node_Connection_weight[row][col]+=1
#print Text_Node_Connection_weight

for Train_Time in range(10):
    for i in range(len(Text_Node)):     
        d = 0.85
        Score = 1-d
        for j in range(len(Text_Node_Connection_weight[i])):
            Score+= d*float(Text_Node_Connection_weight[i][j])*Text_Node_value[i]/float(sum(Text_Node_Connection_weight[j]))
        Text_Node_value[i] = Score
    #print Text_Node_value
#print Text_Node_value.argsort()[-1*Get_Top_Num:][::-1]

TopText = np.sort(Text_Node_value.argsort()[-1*Get_Top_Num:], axis=None) 
#TopText = Text_Node_value.argsort()[-1*Get_Top_Num:][::-1]
for i in TopText:
    print i,Text_Node[i],Text_Node_value[i]

from jieba import analyse

# 基于TextRank算法进行关键词抽取
keywords = analyse.textrank("「東森新聞」顛覆你對新聞的認知，改變你閱讀新聞的習慣！在資訊爆炸的世代，讓你的視野和國際接軌！「東森新聞」名列全球百大頂尖媒體，更是台灣最具代表性的新聞頻道，經年累月聲援民眾傾訴，揭發不法陋習不遺餘力，第一線的貼近採訪，最深度權威的專題內容，除了東森新聞，只有「東森新聞」。")
# 输出抽取出的关键词
for keyword in keywords:
    print keyword + "/",

