#实例4: 网络页面的爬取和存储
#技能包：os模块

import requests
import os
url = "http://image.ngchina.com.cn/2018/0424/20180424121904163.jpg"
root = "C://pics//" #定义根目录
path = root + url.split('/')[-1] #文件存储路径：以/切割的最后一部分（因为url是.jpg结尾）

try:
	#判断根目录是否存在，不存在则用os.mkdir创建
	if not os.path.exists(root): #os.path.exists(path):当一个路径或者文件描述符存在的,返回True
		os.mkdir(root)  	#os.mkdir(path):创建一级目录。os.makedirs（）:创建多级目录。
	
	#判断文件是否存在，不存在则用requests.get方式从网上获得相关文件
	if not os.path.exists(path): 
		r = requests.get(url)    
		with open(path,'wb') as f: 		#open(path,'wb')：二进制形式，覆盖写模式 #with as 语句来简化程式的撰写
			f.write(r.content)    		#r.content 表示返回内容的二进制形式 #图片是二进制格式，将二进制格式保存为文件
			f.close()			   
			print ("文件保存成功")
	else:
		print ("文件已存在")
except:
	print("爬取失败")
	
