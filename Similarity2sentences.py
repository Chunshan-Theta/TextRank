# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
import logging
jieba.setLogLevel(60)
from RKT_class import RKT
import wordfilter as sw



def tk(SourceText):
	seg_list = jieba.lcut(SourceText,cut_all=False)
	seg_list = sw.filter(seg_list)
        num = len(seg_list)
	a = RKT(seg_list,num)
	print SourceText+'\n'
        Out_text =""
	for i in seg_list:Out_text+= i.encode("utf-8")+'/'
        print Out_text+'\n'
	#print "\nTheta , keywords by textrank:"
	#for i in a.Text_Array:print i
	#for i in a.Text_Node_value:print i
	#for i in a.TopText:print i,a.Text_Node[i],a.Text_Node_value[i]
	#for i in a.TopText_H2L:print (a.Text_Node[i]).encode('utf-8')+'/',
        return a.TopText
# 原始文本
SourceText1 = "對每一個決心學習寫程式的工程師來說，入坑之前，你也許只是一個「穿著正裝在辦公室裡上班」的人。你的學習歷程可能是這樣：如同一片樹葉，開始被各種建議拽著走，直到學完了每一個你能想像到的線上課程。最後，雖然你成功拿下了一份軟體開發的工作，但也對工程師有了新的認知：「那些看似正常的工程師們其實都是些『反社會』的怪人，鬼才知道他們經歷了什麼樣的精神創傷。」一份常見的程式學習過程：先從 Ruby 著手。很快，開始穿梭在 Scala, Clojure 和 Go 等其他語言中了。學習了Emacs，接著是 Vim，甚至還了解了 Dvorak 鍵盤佈局。接著又學習了 Linux，甚至還涉獵了 Lisp，以及用 Python 寫過程式，後來一直在命令行駐足半年多。一起來看一下學習寫程式要經歷哪幾個階段：剛開始學習時，你需要理解的東西很少。不論什麼目的、語言或背景，只需要明白一個「for」循環是什麼、如何用條件邏輯框架以及寫程式語言的基本語法。而且基礎知識終究沒有那麼多，所以知識體系在一開始並不複雜。但一旦掌握基礎，需要學習的知識面就一下變寬了，因為你需要了解更複雜的問題，例如了解程式錯誤以及什麼時候用哪些程式碼。這跟回答普通的問題截然不同，這個特殊的問題並沒有一個正確的答案，事情開始複雜起來。當進展到第三階段，知識面開始像氣球一樣膨脹。現在你開始知道需要什麼工具、用什麼程式語言、相關的計算機常識、如何寫模塊化的程式、面對對象寫程式、好的格式以及如何尋求幫助（這只是列舉了一些）。每次去谷歌搜尋或者駭客新聞，你就會發現更多你不知道但感覺要學習的知識。你產生了一個永遠不知道還有什麼不知道的念頭。"


SourceText2 = "「想要在這個資訊知識時代保障工作嗎？快來學寫程式！」這大概是現代社會最常對年輕學生與中年工作者說的話了。放眼望去全世界成功的公司，哪一間沒有成群的工程師作為強力後盾；現在最熱門的地區已經不是工業區，而是那裡的矽谷、這裡的科學園區。任何熟悉 Python、Java，甚至只是 HTML、CSS 之類網頁語言的人，在這個數位化商業市場中可說是炙手可熱，需求快要超越每間公司必備的會計師。不過，雖說寫程式是現在的企業潮流，也不是每個會寫程式的人都能保證有個鐵飯碗。事實上，隨著程式科技的發展，業界已經出現了幾個特別的現象與隱憂，受潮流鼓勵而想一股腦衝去報名程式速成班的人，可能得好好考慮。1）程式世界的競爭不是「擠破頭」就能形容的寫程式既然已經是全球趨勢之一，市場人力競爭程度也不用多說。特別是在印度等開發中國家，許多原先應是一份完整企劃的工作，其實常常被分解成小塊小塊的階段性任務，由 Upwork 國際接案網等等的電腦化服務平台，發送給低薪、高實力的自由工作者或小型工作室。基本上，除了跟普羅大眾一樣忙著投履歷找正職的人之外，寫程式的競爭對手多到排山倒海地能淹沒一個大城市。"

SourceText3 = "新埔鎮是一個正在蛻變中的鄉鎮，兼具傳統與現代，在新竹縣政府與新埔鎮公所合作努力推動之下，正往休閒觀光方面發展，加工產業、特色農產品、客家美食、歷史建築、宗祠、客家文化之旅，都成為甚受歡迎的項目。也因此帶來觀光人潮，一些有想法、有規劃、有目標的年輕人，慢慢回鄉創業，為原本傳統的產業，注入一股新的活力，讓經濟活動更加活絡，也讓到新觀光旅遊的旅者，有了新的服務項目及產品，也為在地的鄉親帶來新的休閒空間。"

SourceText1_ta = tk(SourceText1)
SourceText2_ta = tk(SourceText2)
SourceText3_ta = tk(SourceText3)
from math import log
sametext=[]
for i1 in SourceText1_ta:
    if i1 in SourceText2_ta and i1 not in sametext:
        sametext.append(i1)
print len(sametext)/(log(len(SourceText1_ta))+log(len(SourceText2_ta)))
sametext=[]
for i1 in SourceText1_ta:
    if i1 in SourceText3_ta and i1 not in sametext:
        sametext.append(i1)

print len(sametext)/(log(len(SourceText1_ta))+log(len(SourceText3_ta)))

