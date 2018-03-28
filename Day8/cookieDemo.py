import urllib.request
import http.cookiejar
file = "cookies.txt"
cookie = http.cookiejar.MozillaCookieJar(file)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来
# ignore_expires的意思是如果在该文件中cookies已经存在则覆盖原文件写入
# 在这里，我们将这两个全部设置为True。
# 36运行之后，cookies将被保存到cookie.txt文件中
for each in cookie:
    print(each.name+"="+each.value)