# coding:utf-8
import json 
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
jieba.setLogLevel(60)

def filter(source_text_array,textlenlimit=1):
    filtered_text_array = []
    f = open('stop_words.txt','r')
    Stop_Words_Array=f.readlines()
    for i in range(len(Stop_Words_Array)) :Stop_Words_Array[i] = Stop_Words_Array[i].replace("\n","")


    for i in range(len(source_text_array)):
        #print source_text_array[i]
        if not source_text_array[i].encode('utf-8') in Stop_Words_Array :
            if len(source_text_array[i])>textlenlimit:
                filtered_text_array.append(source_text_array[i])
        else:            
            jieba.Write_Log_Debug('Stop_Words: '+source_text_array[i].encode("utf-8"))
    f.close()
    return filtered_text_array



