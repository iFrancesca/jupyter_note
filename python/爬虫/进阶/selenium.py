import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

## 声明浏览器对象
browser=webdriver.Chrome()

'''
## 访问页面
browser.get('https://www.taobao.com')
print(browser.page_source)
'''

## 查找节点

### 单个节点
'''
input_first=browser.find_element_by_id('q')
input_second=browser.find_element_by_css_selector('#q')
input_third=browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)    
'''
'''
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by__partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''
'''find_element(By,value)\
e.g  find_element(By.ID,id)==find_element_by_id(id)
'''
### 查找多个节点
'''
browser.find_elements_by_css_selector('.service-nd li')
'''

## 节点交互
'''
input=browser.find_element_by_id('q')
input.send_keys('iPhone')   #输入文字
time.sleep(1)
input.clear()                #清空文字
input.send_keys('iPad')
button=browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
button.click()
'''
##动作链
###拖拽
'''
url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_css_selector('#draggable')
target=browser.find_element_by_css_selector('#droppable')   
actions=ActionChains(browser)     #声明ActionChains对象并将其赋值为actions变量
actions.drag_and_drop(source,target)  #调用actions变量的drag_and_drop()方法,再调用perform()方法执行动作
actions.perform()                                        
'''
## 执行JavaScript
'''
browser=webdriver.Chrome()
browser.get('https://zhihu.com/expore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''
## 获取节点信息
#### 获取属性： get_attribute()
'''
browser=webdriver.Chrome()
browser.get('https://zhihu.com/expore')
logo=browser.find_element_by_id('zh-top-link-logo')
print(logo.get_attribute('class'))
'''
#### 获取文本值: 直接调用文本属性
'''
browser=webdriver.Chrome()
browser.get('https://zhihu.com/expore')
input=browser.find_element_by_name('zh-top-add-question')
print(input.text)
'''

#### 获取id、位置、标签名和大小
'''
url='https://www.zhihu.com/explore'
browser.get(url)
input=browser.find_element_by_css_selector('#root > div > div:nth-child(2) > header > div.AppHeader-inner > div.SearchBar > div > form > div > div > label > button > span > svg')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
'''
## 切换Frame
'''

from selenium.common.exceptions import NoSuchElementException 

url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')        #切换到子Frame
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()               #重新切换回父级Frame
logo=browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
'''
## 延时等待
### 隐式等待
'''
import time
url='https://www.zhihu.com/explore'

browser.implicitly_wait(10)
browser.get(url)
input=browser.find_element_by_class_name('zu-top-add-question')
print(input)
'''
### 显式等待
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser,10) #引入WebDriverWait对象，指定最长等待时间
input = wait.until(EC.presence_of_element_located((By.ID,'q')))    #调用wait方法，指定等待条件
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'btn-search')))
print(input,button)
'''
## 前进和后退

'''
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
'''

## Cookies
'''
url='https://www.zhihu.com/explore'
browser.get(url)
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()
'''
## 选项卡管理
'''
import time
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')   #新开启一个选项卡
print(browser.window_handles)
time.sleep(1)
browser.switch_to_window(browser.window.handles[1])
browser.get('https://www.taobao.com/')
'''
## 异常处理
'''
from selenium.common.exceptions import TimeoutException,NoSuchElementException
try:
    browser.get('https://www.python.org/')
except TimeoutException:
    print('Time Out')

try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
'''

# Chrome Headless模式
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)