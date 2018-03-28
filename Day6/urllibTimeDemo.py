import urllib.request
try:
    response = urllib.request.urlopen("http://www.baidu.com",timeout=0.1)
    print(response.read().decode("utf-8"))
    print(response.status)
except urllib.error.URLError as reason:
    print("错误",str(reason))