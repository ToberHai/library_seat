#coding=utf-8

import requests
import datetime
import io

cookies = {} #构建一个空字典用来存放cookies
headers = {
        'Host': '210.44.64.139',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://210.44.64.139/touchscreen/index.php',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '9',
        'Connection': 'keep-alive',
    }


time1 = datetime.datetime.now()
year = time1.year
month = time1.month
day = time1.day

#cardno是学生卡刷卡机上的编码
data = {'cardno':'**********' }

#此处data1用来测试数据，实际并未使用
#data1 = {'order_date': '' ,'room_id':'10' }

#seat_id是预约座位的编号
data2 = {'order_date': (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d") ,'seat_id':'****' }


url = 'http://210.44.64.139/touchscreen/index.php'
s = requests.session()
#response = s.get("url")
response = s.post("http://210.44.64.139/touchscreen/seatOrderAction.php?action=payCardLogin", data=data, headers=headers)
response.encoding='utf-8'
print(response.text)

response = s.post("http://210.44.64.139/touchscreen/seatOrderAction.php?action=addOrderSeat", data=data2, headers=headers )
response.encoding='utf-8'
print(response.text)