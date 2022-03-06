from openpyxl import load_workbook
import http.client
import hashlib
import urllib
import random
import json
import time
import random

wrong=[]

def read(path):
    with open(path,encoding='utf-8') as f:
        text = f.readlines()
        return text
def write(path,content):
    with open(path,'a',encoding='utf-8') as f:
        f.write(content)



#百度翻译接口
def en_to_zh(q):
    appid = '20200803000532562'  # 填写你的appid
    secretKey = 'WLsCcAJeN3L8O9cl533m'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result['trans_result'][0]['dst']

    except Exception as e:
        print('error',e)
        wrong.append(q)
        return str(e)
  
def main(path):
     
    path1 = 'D:\\paper\\wang\\基金委政策局--基础研究两条腿走路\\nsf\\清洗\\{}.txt'.format(path)
    path2 = 'D:\\paper\\wang\\基金委政策局--基础研究两条腿走路\\nsf\\清洗\\man--{}.txt'.format(path)
    path3 = 'D:\\paper\\wang\\基金委政策局--基础研究两条腿走路\\nsf\\清洗\\wrong--{}.txt'.format(path)
    en = read(path1)

    #写入文件

    for i in range(len(en)):
        try:
            write(path2,en[i])
            write(path2,en_to_zh(en[i]))
            write(path2,'\n')
            write(path2,'-'*50)
            write(path2,'\n'*2)
            time.sleep(1)
            print(i,end = ' ')
        except:
            write(path3,en[i])
            print('error',str(i))


    #检查格式

    lt = read(path2)
    for i in range(2,len(lt),4):
        if lt[i][0] != '-':
            print(lt[i-2])
    
    



path = ['出版物']
for p in path:
    print(p+' start')
    main(p)
    print(p+'--ok',end = '\n'+'-'*50+'\n')
