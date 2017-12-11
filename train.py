# coding:utf-8
import json 
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
jieba.setLogLevel(60)
def filter(source_text_array):
    filtered_text_array = []
    f = open('stop_words.txt','r')
    Stop_Words_Array=f.readlines()
    for i in range(len(Stop_Words_Array)) :Stop_Words_Array[i] = Stop_Words_Array[i].replace("\n","")


    for i in range(len(source_text_array)):
        #print source_text_array[i]
        if not source_text_array[i].encode('utf-8') in Stop_Words_Array :
            filtered_text_array.append(source_text_array[i])
        else:
            print 'Stop_Words: ',source_text_array[i]
    f.close()
    return filtered_text_array


def update():
    f = open('train_data','r')
    new = open('stop_words.txt','wa')
    Json_Array = json.loads(f.read())
    Json_value_Array = [int(i) for i in Json_Array.values()]
    q75, q25 = np.percentile(Json_value_Array, [75 ,25])
    iqr = q75 - q25
    print q75+iqr*1.5, q25-iqr*1.5
    for key, value in Json_Array.items():
        if int(value)>q75+iqr*1.5 or int(value)<q25-iqr*1.5:
            new.write(key.encode('utf-8')+'\n')
        else:
            pass
            #print key
    stop_words_default=["「","」","，","！"]
    for i in stop_words_default:
        new.write(i+'\n')
    new.close()

def drop_repeat():
    f = open('stop_words.txt','r')
    Stop_Words_Array_in_txt = f.readlines()
    f.close()
    f = open('stop_words.txt','w')
    Stop_Words_Array = []
    for i in Stop_Words_Array_in_txt:
        if i not in Stop_Words_Array and i != '\n':
            Stop_Words_Array.append(i) 
            f.write('\n'+i)
    f.close()




def train(data_file_name):

    print 'doc/waitfortrain/'+str(data_file_name)+'.txt'
    f = open('doc/waitfortrain/'+str(data_file_name)+'.txt','r')
    seg_list = jieba.lcut(f.read(),cut_all=False)
    #print seg_list
    doc={}
    for i in seg_list:
        if i.encode('utf-8') not in doc.keys():
            doc.update({i.encode('utf-8'):"1"})
        else:
            if i.encode('utf-8') != '\n' and  i.encode('utf-8') != '':
                doc[i.encode('utf-8')] = str(int(doc[i.encode('utf-8')])+1).rstrip()






    
    
    json_data = open('train_data','r')
    Json_Array = json.loads(json_data.read(),encoding="utf-8")
    json_data.close()
    new_data ={}
    Json_Array_new = {}
    new_data.update(doc)
    exist_key = Json_Array.keys()

    for key, value in Json_Array.items():
        Json_Array_new.update({key.encode('utf-8'):value.encode('utf-8')})

    
    for key, value in new_data.items():
        if key.decode("utf-8") !="\n" and key.decode("utf-8")!="":
            if key.decode("utf-8") not in exist_key :
                Json_Array_new.update({str(key):str(value)})
            else:
                update_value = int(Json_Array_new[key])+int(value)
                Json_Array_new[key] = str(update_value)
            


    json_data_string = '{'
    for key, value in Json_Array_new.items():
        #print type(key),type(value)
        #print key,value
        nkv = '"'+key+'":"'+value+'",'
        json_data_string = json_data_string + nkv
    json_data_string = json_data_string[:len(json_data_string)-1]+'}'

    json_data = open('train_data','w')
    json_data.write(json_data_string)
    json_data.close()    
    f.close()
    

'''
a=['the', 'of', 'is','test','qweqwe','wwwwertt','isisisi']
print filter(a)
update()
drop_repeat()
'''

for i in range(1,151):
    train(i)

update()
drop_repeat()


