import requests
import json
link = """https://api-zero.livere.com/v1/comments/list?callback=jQuery112403070970356525906_1522113870624&limit=10&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1522113870626"""
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
r = requests.get(link,headers = headers)
print(r.text)

json_string = r.text
json_string = json_string[json_string.find('{'):-2]
json_data = json.loads(json_string)
comment = json_data['results']['parents']
for each in comment:
    message = each['content']
    print(message)