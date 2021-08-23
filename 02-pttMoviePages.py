import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index{}.html'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

page = 9502
# Request get method to ptt Movie
# use for repeat 5 times
for i in range(0, 5):
    res = requests.get(url.format(page), headers = headers)
    #Get HTML string
    soup = BeautifulSoup(res.text, 'lxml')
    titles = soup.select('div.title')
    # for titleSoup in titles:
    #     try:
    #         title = titleSoup.select('a')[0].text
    #         articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
    #     except IndexError:
    #         print(titleSoup)
    #     print(title)
    #     print(articleUrl)

    for titleSoup in titles:
        if titleSoup.select('a').__len__() == 0:
            continue
        title = titleSoup.select('a')[0].text
        articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
        print(title)
        print(articleUrl)

    page -= 1
