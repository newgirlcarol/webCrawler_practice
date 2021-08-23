import requests
from bs4 import BeautifulSoup
import time

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
        except IndexError:
            pass
        print(title)
        print(articleUrl)

    # Setting timebreak before keep requesting page
    time.sleep(5)

    # Get last page url
    newurl = 'https://www.ptt.cc'+ soup.select('a[class="btn wide"]')[1]['href']
    url = newurl #將前面的url的變數覆蓋，取得新的網址