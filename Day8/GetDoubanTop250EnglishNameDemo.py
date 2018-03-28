import requests
from bs4 import BeautifulSoup
movie_list = []
movie_list2 = []
def get_movie():
    for get_url in range(0,10):
        base_url = "https://movie.douban.com/top250?start="
        item = str(get_url*25)
        url = base_url+item
        r = requests.get(url,timeout = 2000)
        soup = BeautifulSoup(r.text,"xml")
        div_list = soup.find_all('div', class_= "hd")
        for each in div_list:
            english_name_list = soup.find_all("span",class_ = "title")
            for eachone in english_name_list:
                movies = eachone.text.strip("&nbsp;/&nbsp;")
                movie_list2.append(movies)
            return movie_list2
movies = get_movie()
print(movie_list2)
