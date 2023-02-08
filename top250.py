import requests

from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

url = "https://movie.douban.com/top250?start=0&filter="

def find_one_page(url):
    response = requests.get(url, headers=headers, proxies={"https": '127.0.0.1:4780'})
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.find_all("div", class_="hd")
    with open("豆瓣top250.txt","a",encoding='utf-8') as fp:
        for movie in movies:
            title = movie.find("span", class_="title").text
            fp.write(title+"\n")

for i in range(0,10):
    url = "https://movie.douban.com/top250?start={}&filter=".format(i*25)
    find_one_page(url)

print('爬取数据完毕！')