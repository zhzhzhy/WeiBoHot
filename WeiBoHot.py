# -*- coding=UTF-8 -*-
#!/usr/bin/env python3

# import os
import time
import requests
from lxml import etree

# count chinese characters number
def str_count(str):
    zh_count = 0
    for s in str:
        if '\u4e00' <= s <= '\u9fff':
            zh_count += 1
    return zh_count

url = "https://s.weibo.com/top/summary?cate=realtimehot"
headers={
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

r = requests.get(url,headers=headers)
print(r.status_code)
html_xpath = etree.HTML(r.text)
data = html_xpath.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]')
num = -1
data_time = time.strftime('%Y{y}%m{m}%d{d}%H{h}',time.localtime()).format(y='年', m='月', d='日',h='时')
print('{}\n\n'.format(data_time+'数据'))

for tr in (data):
    title = tr.xpath('./a/text()')
    hot_score = tr.xpath('./span/text()')
    length = len(str(num)+title[0])+1       #Total length of row char number
    zh_count = str_count(title[0])          #Number of chinese char(width of two English words)
    indent = 50-(length-zh_count)-2*zh_count   #Indent of blank space
#   print(zh_count)
    num += 1
    # Filter the 0 result
    if num == 0:
        pass
    else:
        print('{}.{}'.format(num,title[0]),'{}'.format(' '*indent+'微博热度:'+hot_score[0]))
