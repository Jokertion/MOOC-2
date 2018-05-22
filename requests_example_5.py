#实例5: IP地址归属地的自动查询
import requests
url = "http://m.ip138.com/ip.asp?ip="

try:
	r = requests.get(url+"219.237.72.34")
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])
except:
	print("爬取失败")
	