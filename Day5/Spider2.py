import pickle
import requests
r = requests.get("http://www.gamersky.com")
print(r.status_code)
f = open("gamer_sky.txt","wb")
r_text = r.text
pickle.dump(r_text,f)
f.close()
print("写入成功")
print(r.url)
print(r.cookies)
print(r.headers)
