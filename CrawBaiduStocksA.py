#CrawBaiduStocksA.py
#百度股票信息爬取
#技能包：requests-bs4-re
#对于非常有特征的数据，直接用re获取，有些数据位置固定，bs4定位到位置上，然后再通过正则表达式获取其中内容
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url): 
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
	
def getStockList(lst,stockURL): #保存股票代码的列表
	html = getHTMLText(stockURL)  #调用函数，获得股票页面
	soup = BeautifulSoup(html,"html.parser")  #解析页面
	a = soup.find_all('a')  #找到所有a标签
	for i in a:  
		try:
			href = i.attrs['href']   #获取a标签href属性的内容
			lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
		except:
			continue
	
def getStockInfo(lst, stockURL, fpath): #获得个股信息
	for stock in lst:
		url = stockURL + stock + '.html'  #获得网址
		html = getHTMLText(url)    #获取页面内容
		try:
			if html == '':
				continue
			infoDict = {}  #所有个股信息
			soup = BeautifulSoup(html,'html.parser')  #解析网页类型
			stockInfo = soup.find('div', attrs={'class':'stock-bets'})
			
			name = stockInfo.find_all('a',attrs={'class':'bets-name'})[0]
			infoDict.update({'股票名称:':name.text.split()[0]})
			
			keyList = stockInfo.find_all('dt')  #股票信息的键 列表
			valueList = stockInfo.find_all('dd') #股票信息的值 列表
			for i in range(len(keyList)): #将键和值封装进字典中
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val

			with open(fpath, 'a', encoding='utf-8') as f: #保存信息到文件中
				f.write( str(infoDict) + '\n' )
		except:
			traceback.print_exc() #获得异常的错误信息
			continue
	
def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html#sz' #获得股票列表
	stock_info_url = 'https://gupiao.baidu.com/stock/' #获得个股信息
	output_file = 'D:/BaiduStockInfo2.txt' #输出文件保存目录
	slist = [] #股票信息
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url,output_file)

main()
