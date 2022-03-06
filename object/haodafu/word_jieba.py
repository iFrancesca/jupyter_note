# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:33:05 2021

@author: 11581
"""

import wordcloud
import jieba
from imageio import imread


def cut_word(txt):
    for ch in ''' :：'，。, :？！、“”（）''':
        txt = txt.replace(ch,"")
    words=jieba.lcut(txt)
    counts={}
    for word in words:
    #找到想要的词语
        if word in ['您','您好','谢谢','谢谢','请','你好','祝您','早日康复','客气'\
                    ,'祝','顺心','~']:
            counts[word]=counts.get(word,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    return items

'''   
#输入文件名
txt=open('d:/python/spyder/文件/豆瓣电影_评论.txt,encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    #剔除不想要的词语
    if word in ['一个','就是','这个','自己','我们','可以','可能','没有','还是',\
                '所以','不是','已经','但是','那么','其实','他们','大家','觉得','因为'\
                ,'成为']:
        continue
         
    #elif len(word)==1:
     #   continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
'''
'''
#可以自定义初始的dic

for i in range(100):
    word,count=items[i]
    print('{:<15}{:>5}'.format(word,count))
    
    dic[word]=dic.get(word,0)+count


mask=imread('fivestart.png')
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc",mask=mask    
    )
#按频率，否则使用w.generate(txt)
w.fit_words(dic)
#输入保存文件
w.to_file("唐探33.png")
'''