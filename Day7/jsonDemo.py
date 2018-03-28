import requests
import json
def getComment(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    r = requests.get(url,headers = headers,timeout = 200000)
    json_string = r.text
    json_data = json.loads(json_string)
    comment = json_data["partial"]
    for each in comment:
        user = each["node"]["user_name"]
        message = each["node"]["body"]
        print(user+":"+message)
for page in range(0,7):
    url1="https://www.g-cores.com/comments?commentable_type=article&commentable_id=97238&page="
    url2="&sort=hot"
    page_str = str(page)
    link = url1+page_str+url2
    getComment(link)