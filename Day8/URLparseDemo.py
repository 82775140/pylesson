from urllib.parse import urlparse
response = urlparse("http://www.zhihu.com/question/33313562?sort=created",scheme='https',allow_fragments=False)
print(response)