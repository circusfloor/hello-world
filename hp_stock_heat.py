#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import csv
import os

def getHTMLText(url, t):
    """html获取"""
    try:
        kv = {'user-agent': 'Chrome/98'}
        r = requests.get(url, headers=kv)
        if t == 1:
            r.encoding = 'gbk'
            r = r.text
            return r
        else:
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r
    except:
        return '产生异常'

url = r'https://bbs.hupu.com/stock'
html = getHTMLText(url, 2)
soup = BeautifulSoup(html.content, 'html.parser')
heat = soup.find('span', text='话题热度').next_sibling.text
time = datetime.now().strftime('%Y%m%d %H%M%S')


cols = ['时间', '热度']
if os.path.exists('hp_stock_heat.csv'):
    with open('hp_stock_heat.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writerow({'时间': time, '热度': heat})
else:    
    with open('hp_stock_heat.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        writer.writerow({'时间': time, '热度': heat})
    

