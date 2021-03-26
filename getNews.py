# -*- coding:utf8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='test', charset='utf8')
cursor = conn.cursor()
import datetime
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('http://www.pingcheng.gov.cn/pcqrmzf/zcfw/list_2.shtml')
titles = r.html.find('.news_list > li > a')

datalist = []
sql = "insert into table_text (title,url,create_time,content,source,publishDate) values (%s,%s,%s,%s,%s,%s)"
for title in titles:
    mytitle = title.text.encode('utf-8')
    myurl = list((title.absolute_links))[0]
    create_time = datetime.datetime.now()
    connectUrl = ((str(title.absolute_links).replace('{', '')).replace('}', '')).replace('\'', '')
    connectSession = session.get(connectUrl)
    source = list(connectSession.html.xpath('/html/body/div/div[3]/div[2]/span[2]/text()'))[0]
    mysouce = source.replace("来源：", "")
    publishDate = list(connectSession.html.xpath('/html/body/div/div[3]/div[2]/span[1]/text()'))[0]
    mydate = publishDate.replace("发布时间：", "")
    contents = ''
    connect = connectSession.html.find('body > div > div.main_body.main_content.clearfix > div.content')
    for connectText in connect:
        text = connectText.text
        contents += text
    datalist.append((mytitle, myurl, create_time, contents, mysouce, mydate))
cursor.executemany(sql, datalist)
print(datalist)
conn.commit()
cursor.close()
conn.close()
