# library_seat

### 9.18更新

更新规则：仅能预约当前一天位置

### 8.22更新

1.采用多线程post方式
2.增加持续时间
3.提高可靠性

本次更新请使用命令行 `python lib_bate_threads.py` 运行脚本
代码参考CSDN https://blog.csdn.net/henni_719/article/details/73201302
	
### 如果使用本脚本，请您具备以下条件

1.一台24h开机的电脑

2.安装python环境以及requests环境库

3.学会使用百度或Google等搜索引擎

### 下面是使用步骤

1.下载代码并解压

2.修改cardno,seat_id的值

 cardno值可以在打卡机器上获取

 seat_id值可以通过F12开发者工具获取 例如189的seatid为531
 ![seat](/pic/seat_id.png)

3.安装<a href="https://jingyan.baidu.com/article/ce09321b94a1272bfe858f5a.html" target="_blank">Python环境</a>，并使用pip安装request库

4.打开cmd命令行，运行 `python lib_bate.py`

![cmd](/pic/cmd.png)
![hc](http://107.150.11.135:8181/?/images/2020/08/14/mVE1bdnc5Y/%7BBAD5C565-33BF-4554-8A74-0C9889DD8CA2%7D.png)
#### 如需定时任务，Windows可以使用任务计划程序，具体如何请参见百度
#### Linux……，玩Linux的都是大佬，请自行解决

-----------
仅限参考学习使用，不用于任何商业用途。若有侵权行为，将会在24小时内删除
