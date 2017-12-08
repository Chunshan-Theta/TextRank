# coding:utf-8

def filter(source_text_array):
    filtered_text_array = []
    f = open('stop_words.txt','r')
    Stop_Words_Array=f.readlines()
    for i in range(len(Stop_Words_Array)) :Stop_Words_Array[i] = Stop_Words_Array[i].replace("\n","")


    for i in range(len(source_text_array)):
        #print source_text_array[i]
        if not source_text_array[i].encode('utf-8') in Stop_Words_Array :
            filtered_text_array.append(source_text_array[i])
    return filtered_text_array
'''
a=['the', 'of', 'is','test','qweqwe','wwwwertt','isisisi']
print filter(a)
'''


