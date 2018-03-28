import requests
from bs4 import BeautifulSoup
import lxml
def get_movies():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36","Host":"movie.douban.com"}
    movie_list = []
    for i in range(10):
        link = "https://movie.douban.com/top250?start=" + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i + 1), "响应码:", r.status_code)
        soup = BeautifulSoup(r.text,'xml')
        div_list = soup.find_all('div',class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    print(movie_list)
movies = get_movies()