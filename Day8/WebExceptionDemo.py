import urllib.error
import urllib.request
import socket
try:
    response = urllib.request.urlopen("http://www.cuqingcai.com//index.htm",timeout=0.01)
except urllib.error.URLError as e:
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print("Time OUT")