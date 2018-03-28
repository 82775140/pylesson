import requests
url ="http://img1.gamersky.com/upimg/pic/2018/03/28/small_201803280651236677.jpg"
r = requests.get(url)
with open ("pic.jpg","wb") as file:
    file.write(r.content)
    file.close()