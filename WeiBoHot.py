# -*- coding=UTF-8 -*-
#!usr/bin/python

# import os
import time
import requests
from lxml import etree

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
    
    num += 1

    # 过滤第 0 条
    if num == 0:
        pass
    else:
            print('{}.{}\n'.format(num,title[0]))
            print('{} {}\n\n'.format('微博热度：',hot_score[0]))
