import urllib.request
url="http://www.douban.com/"
#请求
request=urllib.request.Request(url)

#爬取结果
response=urllib.request.urlopen(request)

data=response.read()
#设置编码方式
data=data.decode('utf-8')
#打印结果
print(data)

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())