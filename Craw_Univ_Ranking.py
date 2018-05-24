#Craw_Univ_Ranking.py
#定向爬取实例1：2018中国大学排名爬虫
#获得技能包：解决format中文输出对齐问题: char(12288)(采用中文字符的空格填充)

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try :
		r = requests.get(url,timeout = 30)
		r.raise_for_status()  #产生异常信息
		r.encoding = r.apparent_encoding  #修改编码
		return r.text
	except:
		return ""

def fillUnivList(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:   #查找<tbody>标签 并对它的孩子做遍历
		if  isinstance(tr,bs4.element.Tag):  # 作用：检测<tr>标签的类型。如果不是bs4定义的TAG类型，则过滤掉
			tds = tr('td') #将所有td标签存为tds列表
			ulist.append([tds[0].string,tds[1].string,tds[3].string]) #把需要的标签加入到列表中

def printUnivList(ulist,num):
	tplt = "{0:^10}\t{1:{3}^12}\t{2:>2}"
	print(tplt.format("排名","学校名称","总分",chr(12288)))  #表头的打印
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
	html = getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,100)  #100 univs
main()



"""
<tbody class="hidden_zhpm" style="text-align: center;">
		<tr class="alt"><td>1</td><td><div align="left">清华大学</div></td><td>北京</td><td>95.3</td><td class="hidden-xs need-hidden indicator5">100.0</td><td class="hidden-xs need-hidden indicator6"style="display: none;">97.50%</td><td class="hidden-xs need-hidden indicator7"style="display: none;">1182145</td><td class="hidden-xs need-hidden indicator8"style="display: none;">44730</td><td class="hidden-xs need-hidden indicator9"style="display: none;">1.447</td><td class="hidden-xs need-hidden indicator10"style="display: no"""
		
		
		
		