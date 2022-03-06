# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:46:58 2021

@author: 11581
"""

import Cdate
import datetime

'''
lt_le2 = list([] for i in range(4))
cells = ["I","J","K","L"]
for i in range(4):
    cell = "{}2:{}23221".format(cells[i])
    cells_le2 = ws[cell]
    get_lt(cells_le2,lt_le2[i])
print("write_url_ok")

'''

'''
le2 = []
cells_le2 = ws["K2:K664"]
get_lt(cells_le2,le2)
print("read_second_ok")

dic = Cdic.lt_to_dic(le,le2)
fun_dic = Cdic.fun_date(dic)
Cdic.write_dic(fun_dic,ws2)
wb.save(path)
print('write_ok')  
'''


#在一个字典中加入指定列表作为指定键的值 
def lt_to_dic(lt,lt2):
    #将lt2的某些值作为value,lt中的值作为key
    d = dict()
    for i in range(len(lt)):
        key = lt[i]
        value = lt2[i]
        if key in d:
            d.get(key).append(value)
        else:
            d[key] = []
            d.get(key).append(value)
    return d

'''
#字典排序
def dic_sort(d):    
    lt_key = list(d.keys())
    lt_value = list(d.values())
    lt_num = list(map(len,lt_value))

    #lt_speak = [["A","b"],["e","t"]]--->元素为列表--->处理为str
    for i in range(len(lt_speak)):
        s = str(lt_speak[i])
        lt_speak[i] = func(s)
        
'''
#处理字典：每个key对应的value值<value为一包含日期的列表>之差

def fun_date(dic):
    fun_dic = {}
    keys = list(dic.keys())
    
    
    for key in keys:
        value = dic.get(key)
        value.sort()
        if type(value[0])==str:
            new_value = [Cdate.Caltime(value[i],value[i+1]) for i in range(len(value)-1)]
        elif type(value[0])==datetime.datetime:
            new_value = [(value[i+1]-value[i]).days for i in range(len(value)-1) ]
            
        fun_dic[key] = new_value
    
    return fun_dic
    
    
#字典写入文件
'''
字典格式为 {str:list}
写入文件的格式为: 
    str:list[0]
    str:list[1]
    ......

'''    
def write(index,ws,lt):
    for i in range(len(lt)):
        ws.cell(2+i,index).value = lt[i]
    print("write_lt_ok")
            #选择填入某行的单元格
            
def write_dic(dic,ws):
    key_lt = []
    value_lt = []
    for key in dic:
        value = dic[key]
        key_lt.extend([key for i in range(len(value))])
        value_lt.extend(value)
    
    write(10,ws,key_lt)
    write(11,ws,value_lt)
    
    print("write_dic_ok!")
    
    
    
    
    
    
