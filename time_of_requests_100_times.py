#time_of_requests_100_times.py
#爬取QQ音乐100次计时
#技能包：requests库，time模块，爬取异常处理框架
import time 
import requests

def gethtmltext(url):
	try:
		r= requests.get("https://y.qq.com/")
		r.raise_for_status()
		r.encoding = r.apparent_encoding()
		return r.text
	except:
		return "产生异常"
		
if __name__=='__main__':
	url = "https://y.qq.com/"
	total_time = 0
	for i in range(1,101):
		start_time = time.time()
		gethtmltext(url)
		end_time = time.time()
		print ("第{0}次爬取耗时: {1:.3f}秒.".format(i,end_time-start_time))
		total_time += end_time - start_time		#迭代累计总时间(开始总时间为0,然后等式为:a += xxx-xx)
	print("总计爬取耗时: {:.3f}秒.".format(total_time))