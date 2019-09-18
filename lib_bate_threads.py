#coding=utf-8

import requests
import datetime
import time
import io
import threading
from random import randint,choice

cookies = {} #构建一个空字典用来存放cookies
headers = {
        'Host': '210.44.64.139',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': 'http://210.44.64.139/touchscreen/index.php',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '32',
        'Connection': 'keep-alive',
    }


time1 = datetime.datetime.now()
year = time1.year
month = time1.month
day = time1.day

#cardno是学生卡刷卡机上的编码
data = {'cardno':'**********' }

#seat_id是预约座位的编号
data2 = {'order_date': datetime.datetime.now().strftime("%Y-%m-%d") ,'seat_id':'****' }

#登录
url = 'http://210.44.64.139/touchscreen/index.php'
s = requests.session()
response = s.post("http://210.44.64.139/touchscreen/seatOrderAction.php?action=payCardLogin", data=data, headers=headers)
response.encoding='utf-8'
print(response.text)

def postRequest():
	try:
		s.post("http://210.44.64.139/touchscreen/seatOrderAction.php?action=addOrderSeat", data=data2, headers=headers )
		#response = s.post("http://210.44.64.139/touchscreen/seatOrderAction.php?action=addOrderSeat", data=data2, headers=headers )
		#response.encoding='utf-8'
		#print(response.text)
		print("post done")
		pass
	except Exception as e:
		print("error")
		raise e
	pass

def run(threadNum,internTime,duration):
	#创建数组存放线程
	threads=[]
	try:
		#创建线程
		for i in range(1,threadNum):
			#根据函数创建线程
			t = threading.Thread(target = postRequest)
			#把创建的线程加入线程组
			threads.append(t)
		
	except Exception as e:
		raise e
	
	try:
		#启动线程
		for thread in threads:
			thread.setDaemon(True)
			thread.start()
			time.sleep(internTime)
		#等待所有线程结束
		for thread in threads:
			thread.join(duration)
	except Exception as e:
		raise e

if __name__ == '__main__':
	startime=time.strftime("%Y%m%d%H%M%S")

	now=time.strftime("%Y%m%d%H%M%S")
	#设置持续时间
	duratiion=120
	print (duratiion)
	while (startime+str(duratiion))!=now:
		run(20,0.08,int(duratiion))
		now=time.strftime("%Y%m%d%H%M%S")
