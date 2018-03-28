from urllib.parse import urlencode
base_url="http://www.baidu.com?"
params = {"name":"germey","age":22}
url = base_url+urlencode(params)
print(url)