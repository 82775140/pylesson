import urllib.request
proxy_hander = urllib.request.ProxyHandler({"http":"http://127.0.0.1:9743","https":"https://127.0.0.1:9743"})
openurl = urllib.request.build_opener(proxy_hander)
response = openurl.open("http://www.baidu.com")
print(response.read())