import requests
from bs4 import BeautifulSoup
import csv


def spider(page):
    url = 'https://movie.douban.com/top250?start=%d&filter=' % page
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    html = requests.get(url=url, headers=header).text
    return html


def analysis():
    filmName = []
    score = []
    for n in range(0, 250, 25):
        html = spider(n)
        soup = BeautifulSoup(html, 'html.parser')
        hdList = soup.find_all('div', attrs={'class': 'hd'})
        spanList = soup.find_all('span', attrs={'class': 'rating_num'})
        for obj in hdList:
            filmName.append(obj.a.span.text)
        for obj in spanList:
            score.append(obj.text)
    result = zip(filmName,score)
    with open('doubanTop250film.csv', 'w', encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['电影名','评分'])
        writer.writerows(result)

analysis()
