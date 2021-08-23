import requests
from bs4 import BeautifulSoup
import time
import os

# open a new file
if not os.path.exists('./pttMovie'):
    os.mkdir('./pttMovie')

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

for i in range(0,5):
    # Request get method to ptt Movie
    res = requests.get(url, headers = headers)
    #Get HTML string
    soup = BeautifulSoup(res.text, 'lxml')

    #Get all titles and url with tag <a>
    # select回傳結果是list
    titles = soup.select('div.title')
    for titleSoup in titles:
        try:
            title = titleSoup.select('a')[0].text
            articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
            # Get article content
            resArticle = requests.get(articleUrl, headers=headers)
            soupArticle = BeautifulSoup(resArticle.text, 'lxml')
            # articleContent = soupArticle.select('div#main-content')[0].text.split('※ 發信站')[0]
            articleContentSoup = soupArticle.select('div#main-content')[0]
            # for i in articleContentSoup.select('div'):
            #     i.extract()
            # for i in articleContentSoup.select('span'):
            #     i.extract()
            #前兩段回圈合併成一組回圈如下
            for tag in ['div', 'span']:
                for i in articleContentSoup.select(tag):
                    i.extract()
            articleContent = articleContentSoup.text
            # print(articleContent)
            print(title)
            print(articleUrl)
            try:
                with open('./pttMovie/{}'.format(title), 'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except FileNotFoundError:
                title = title.replace('/', '-')
                with open('./pttMovie/{}'.format(title), 'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except OSError:
                pass
        except IndexError:
            pass



    # Setting timebreak before keep requesting page
    time.sleep(5)

    # Get last page url
    newurl = 'https://www.ptt.cc'+ soup.select('a[class="btn wide"]')[1]['href']
    url = newurl