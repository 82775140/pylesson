import requests
url = "http://www.baidu.com/s"
headers = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36","Host: www.baidu.com"}
key_dict = {"wd":"name%20germey"}
res = requests.get(url = url,params=key_dict)
print(res.url)