# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
import logging
jieba.setLogLevel(60)
from RKT_class import RKT
import train as sw

seg_list = jieba.lcut("民進黨原打算上月二十三日完成《勞動基準法》初審，因在野黨強力杯葛，黨內也出現雜音，修法延宕，上周經閣揆賴清德兩度親自與綠委溝通後，已就爭議較大的「鬆綁七休一」及「輪班間隔」部分達成共識，其中鬆綁七休一部分將由勞動部主動公告適用行業；輪班間隔原則十一小時，增訂八小時的例外特殊狀況，須經目的事業主管機關會同勞動部核准，雙重把關機制。勞團批修法仍有過勞疑慮；工總則認為，若都要經主管機關認定，緩不濟急。",cut_all=False)


seg_list = sw.filter(seg_list)



a = RKT(seg_list)
for i in a.Text_Node_value:pass #print i
for i in a.TopText:print i,a.Text_Node[i],a.Text_Node_value[i]

