# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import xlwt

def get_content():
    url = 'https://xiaoyuan.zhaopin.com/full/538/0_0_160000_1_0_0_0_1_0'
    a = urllib.request.urlopen(url)
    html = a.read().decode('utf-8')
    return html

def get(html):
    reg = re.compile(r'class="searchResultJobName">.*?<a joburl href="//(.*?)" class="fl __ga__fullResultcampuspostname_clicksfullresultcampuspostnames_001">(.*?)</a>.*?<p class="searchResultCompanyname"><span>(.*?)</span>.*?<span>发布时间：<em>(.*?)</em></span>.*?职责描述：<span>(.*?)</span>',re.S)
    items = re.findall(reg,html)
    items_length = len(items)
    return items,items_length

def excel_write(items,index):
    for item in items:
        for i in range(0,5):
            ws.write(index,i,item[i])
        print(index)
        index+=1

newTable="智联招聘岗位爬虫结果.xls"
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('sheet1')
headData = ['url','职位','公司','发布时间','职责描述']
for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))

index = 1
items,items_length = get(get_content())
excel_write(items,index)
wb.save(newTable)