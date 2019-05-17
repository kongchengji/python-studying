# -*- coding: utf-8 -*-
import requests
import re

#下载一个网页
url = 'http://www.linlida.com/0_646/'
#模拟浏览器发送HTTP请求
response = requests.get(url)
#修改编码方式
#response.encoding = "utf-8"
response.encoding = "gbk"
#目标小说主页网页源码
html = response.text
#获取每一章小说的信息（章节,url）
dl = re.findall(r'<dl>.*?</dl>',html,re.S)[0]
chapter_list = re.findall(r'<dd><a href="(.*?)">(.*?)</a></dd>',dl)
#获取小说名字
title = re.findall(r'<h1>(.*?)</h1>',html)
print(title)
#新建一个txt，保存小说内容
fb = open('%s.txt' %title,'w',encoding='utf-8')
#循环每一个章节，分别去下载(前10个章节)
for chapter_info in chapter_list[:10]:
    chapter_url,chapter_name = chapter_info
    chapter_url = 'http://www.linlida.com%s' % chapter_url

    #下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'gbk'
    #提取章节内容
    chapter_text = re.findall(r'<div id="content">(.*?)</div>',chapter_response.text,re.S)[0]
    #清洗章节数据
    chapter_text = chapter_text.replace(' ','')
    chapter_text = chapter_text.replace('&nbsp;', '')
    chapter_text = chapter_text.replace('<br/>', '')
    #持久化
    fb.write(chapter_name)
    fb.write('\n')
    fb.write(chapter_text)
    fb.write('\n')






