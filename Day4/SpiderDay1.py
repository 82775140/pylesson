import requests
r = requests.get("http://www.baidu.com/")
print("文本文件", r.encoding)
print("响应码", r.status_code)
print("字符串方式的响应体",r.text)