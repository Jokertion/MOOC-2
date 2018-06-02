#CrawBaiduStocksB.py 
#百度股票信息爬取 优化
#优化内容： 1.将动态解析编码格式改为直接给出编码格式（省时）
#	    2.增加爬取进度条（增加用户体验） 
#对于非常有特征的数据，直接用re获取，有些数据位置固定，bs4定位到位置上，然后再通过正则表达式获取其中内容

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url, code="utf-8"): 
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ""

def getStockList(lst, stockURL):  		   #保存股票代码的列表
	html = getHTMLText(stockURL, "GB2312")     #调用函数，获得股票页面
	soup = BeautifulSoup(html, 'html.parser')  #解析页面
	a = soup.find_all('a') 			   #找到所有a标签
	for i in a:  
		try:
			href = i.attrs['href']     #获取a标签href属性的内容
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
			continue

def getStockInfo(lst, stockURL, fpath):		   #获得个股信息
	count = 0
	for stock in lst:
		url = stockURL + stock + ".html"  #获得网站
		html = getHTMLText(url)   	  #获取页面内容
		try:
			if html=='':
				continue
			infoDict = {} 		  #所有个股信息
			soup = BeautifulSoup(html, 'html.parser')    #解析网页类型
			stockInfo = soup.find('div',attrs={'class':'stock-bets'})
			
			name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
			infoDict.update({'股票名称': name.text.split()[0]})
			
			keyList = stockInfo.find_all('dt') 	     #股票信息的键 列表
			valueList = stockInfo.find_all('dd')         #股票信息的值 列表
			for i in range(len(keyList)): 		     #将键和值封装进字典中
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val

			with open(fpath, 'a', encoding='utf-8') as f:   #保存信息到文件中
				f.write( str(infoDict) + '\n' )
				count = count + 1
				print('\r当前进度：{:.2f}%'.format(count*100/len(lst)),end="")
		except:
			count = count + 1
			print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
			continue

def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'	 #获得股票列表
	stock_info_url = 'https://gupiao.baidu.com/stock/'		 #获得个股信息
	output_file = 'D:/BaiduStockInfo.txt'				 #输出文件保存目录
	slist=[] 							 #股票信息
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)

main()


'''
错误总结：
1.（44）infoDict.update=({'股票名称': name.text.split()[0]}) --》多打了个等号
2.(64)stock_info_url = 'https://gupiao.baidu.com/stock' --》末尾少打个/
3.(65)output_file = 'D://BaiduStockInfo.txt'  --》 D:/ 路径多打一个/
'''
