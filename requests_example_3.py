#实例3: 百度/360搜索关键词提交
#技能包：找出网页的API
'''
百度/360搜索关键词接口：
http://www.baidu.com/s?wd=keyword
http://www.so.com/s?q=keyword
'''
import requests
keyword = "韩帼眉"
try:
	kv = {'wd':'韩帼眉'}
	r = requests.get("http://www.baidu.com/s",params=kv)
	print (r.request.url)
	r.raise_for_status()
	print (len(r.text))
except:
	print("爬取失败")
	
