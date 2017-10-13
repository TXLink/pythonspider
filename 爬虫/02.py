''''' 
伪装浏览器 
 
对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。 
所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。 
具体实现：自定义网页请求报头。 
'''  


import urllib.request,os
#定义保存函数
def saveFile(data):
    path="D:\\python\\pythonspider\\output\\1.txt"
    f = open(path,'wb') 
    f.write(data) 
    f.close()

url="https://www.baidu.com"
hds={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}
req=urllib.request.Request(url=url,headers=hds)
res=urllib.request.urlopen(req)
data=res.read()

saveFile(data)

#data=data.decode('utf-8')
#print(data)
