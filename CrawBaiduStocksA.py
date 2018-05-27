#CrawBaiduStocksA.py
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

def getStockList(lst, stockURL):
	html = getHTMLText(stockURL)
	soup = BeautifulSoup(html, 'html.parser') 
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
			continue

def getStockInfo(lst, stockURL, fpath):
	for stock in lst:
		url = stockURL + stock + ".html"
		html = getHTMLText(url)
		try:
			if html=="":
				continue
			infoDict = {}
			soup = BeautifulSoup(html, 'html.parser')
			stockInfo = soup.find('div',attrs={'class':'stock-bets'})

			name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
			infoDict.update({'股票名称': name.text.split()[0]})

			keyList = stockInfo.find_all('dt')
			valueList = stockInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val

			with open(fpath, 'a', encoding='utf-8') as f:
				f.write( str(infoDict) + '\n' )
		except:
			traceback.print_exc()
			continue

def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = 'D:/BaiduStockInfo.txt'
	slist=[]
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)

main()
