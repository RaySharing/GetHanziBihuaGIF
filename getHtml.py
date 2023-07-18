#!/usr/bin/python3
from lxml import etree
import requests
import os


# 获取笔画GIF函数
def GetHanzBishun(SearchWord):
    # 获取该汉字的百度链接
    url = "https://hanyu.baidu.com/s?wd=" + SearchWord + "&cf=rcmd&t=img&ptype=zici"
    # 读取url请求内容
    req = requests.get(url)
    req.encoding = 'utf-8'
    # 获取该汉字的页面
    html = etree.HTML(req.text)
    # 定位笔顺动图元素
    result = html.xpath('//img[@id="word_bishun"]/@data-gif')
    return result

# 笔画获取主体
File1 = open("words2.txt", 'r', encoding='UTF-8')
path = "./picture"
os.mkdir(path)
for words in File1:
    SearchWord = words
    picUrl = GetHanzBishun(SearchWord)
    # 获取文件名 MD5名
    filename = os.path.splitext(os.path.basename(str(picUrl)))
    # 获取gif图片内容
    resp = requests.get(picUrl[0])
    resp.encoding='utf-8'
    # 将读取到的文件进行保存
    f = open('./picture/'+filename[0]+'.gif', 'wb')
    f.write(resp.content)
    f.close()
