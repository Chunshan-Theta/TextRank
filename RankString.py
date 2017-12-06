# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_tw/')
import jieba
import logging
jieba.setLogLevel(10)



seg_list = jieba.cut("要求賴院長提出礦業法修法時程",cut_all=False)



Text_Array =[]
Text_Node =[]
Text_Node_Connection = []

for i in seg_list:
    Text_Array.append(i)
print '/'.join(Text_Array)


WindowsSize = 3
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


Text_Node_Connection_weight = np.zeros((len(Text_Node), len(Text_Node)),int)
Text_Node_value = np.arange(float(len(Text_Node)))

for i in range(len(Text_Node_value)):
    Text_Node_value[i]=1
#print Text_Node_value
    

for i in range(len(Text_Node_Connection)):
    Text_Node_Connection[i][0] = Text_Node.index(Text_Node_Connection[i][0])
    for j in range(len(Text_Node_Connection[i][1])):
        Text_Node_Connection[i][1][j]=Text_Node.index(Text_Node_Connection[i][1][j])

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
    print Text_Node_value
#print Text_Node_value.argsort()[-1*Get_Top_Num:][::-1]
Get_Top_Num = int(len(Text_Node)/3)

for i in Text_Node_value.argsort()[-1*Get_Top_Num:][::-1]:
    print Text_Node[i]



