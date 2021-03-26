import requests

url = 'http://zspctst.wt.com:14331/hand-city-web/manage/zsNews/doSave'
headers = {
    'Cookie': 'SESSION=OGE5ZmM3NTAtNDg2Ny00YmZhLWI4YTQtNzVmMjY3MDY5M2U3'
}
data = {
    "thumb": "",
    "tabId": "c0f6ee4c77824522a7fe035e870b144b",
    "praiseCount": "",
    "content": "<p>测</p>",
    "publishDate": "2021-03-16",
    "shareCount": "23",
    "source": "测",
    "storeCount": "",
    "title": "测",
    "recommend": "0",
    "toped": "0",
    "tabName": "动态",
    "status": "1",
    "_nickname": "初见",
    "_institution": "系统运维中心",
    "_userType": "超级用户"
}
response = requests.post(url, headers=headers, data=data)
print(response.text)
