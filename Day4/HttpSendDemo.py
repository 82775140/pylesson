import requests
import pickle
response = requests.get("http://www.g-cores.com")
print(response.headers)
print(response.status_code)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
response = requests.get("http://www.g-cores.com",headers = headers)
print(response.status_code)
GIF = requests.get("https://alioss.g-cores.com/assets/afuxxd/ios-text-772c9257cfcc77962b1e565448c57aaab428e68c2f70d43b99948c6237be3f41.png")
print(GIF.content)
with open("g-cores.png","wb") as f:
    f.write(GIF.content)
    f.close()

