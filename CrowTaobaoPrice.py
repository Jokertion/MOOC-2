#CrowTaobaoPrice.py
#淘宝商品比价定向爬虫
#技能包： 正则表达式
import requests
import re

def getHTMLText(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
	
def parsePage(ilt,html): #从商品页面中获取商品的名称和价格
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price ,title])
	except:
		print("")
	
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"  #定义打印模板
	print(tplt.format("序号","价格","商品名称")) #打印表头
	count = 0  #输出信息计数器
	for g in ilt:
		count = count + 1 #count：商品序号
		print(tplt.format(count, g[0],g[1]))

def main():
	goods = '玛卡'
	depth = 3		#爬取深度
	start_url = 'https://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url +'&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList,html)
		except:
			continue
	printGoodsList(infoList)
	
main()
			

"""
书包_淘宝搜索

https://s.taobao.com/search?q=书包&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180525&ie=utf8
https://s.taobao.com/search?q=书包&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180525&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
https://s.taobao.com/search?q=书包&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180525&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88	
https://s.taobao.com/search?q=书包&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180525&ie=utf8&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132

"""	
	
	
	
	
	
	
	
	