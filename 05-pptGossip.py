import requests
import time
import os
from bs4 import BeautifulSoup

file_path = './ptt_Gossiping'
if not os.path.exists(file_path):
    os.mkdir(file_path)

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
ss = requests.session()
ss.cookies['over18'] = '1'

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

#最外層回圈，爬取多頁
for i in range(0, 30):
    # Get gossip HTML
    res = ss.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    # Get article title
    article_titles = soup.select('div.title')

    for article_title in article_titles:
        try:
            eachTitle = article_title.select('a')[0].text
            titleUrl = 'https://www.ptt.cc' + article_title.select('a')[0]['href']
            article_res = ss.get(titleUrl, headers = headers)
            article_soup = BeautifulSoup(article_res.text, 'lxml')
            print(eachTitle)
            push_up = 0
            push_down = 0
            score = 0
            author = ''
            title = ''
            datetime = ''

            article_content = article_soup.select('div#main-content')[0].text.split('※ 發信站')[0]
            push_info_list = article_soup.select('div[class="push"] span')
            for info in push_info_list:
                if '推' in info.text:
                    push_up += 1
                if '噓' in info.text:
                    push_down += 1
            # 文章資訊
            article_info_list = article_soup.select('div[class="article-metaline"] span')
            for index, list in enumerate(article_info_list):
                if index == 1:
                    author = list.text
                if index == 3:
                    title = list.text
                if index == 5:
                    datetime = list.text
            score = push_up - push_down
            article_content += '\n---split---\n'
            article_content += '推: {}\n'.format(push_up)
            article_content += '噓: {}\n'.format(push_down)
            article_content += '分數: {}\n'.format(score)
            article_content += '作者: {}\n'.format(author)
            article_content += '標題: {}\n'.format(title)
            article_content += '時間: {}\n'.format(datetime)

            try:
                with open('./ptt_Gossiping/{}.txt'.format(eachTitle), 'w', encoding='utf-8') as w:
                    w.write(article_content)
                print()
            except FileNotFoundError:
                pass
            except OSError:
                pass


        except IndexError:
            pass
    time.sleep(5)
    newUrl = soup.select('div.btn-group-paging')[0].select('a')[1]['href']
    url = 'https://www.ptt.cc' + newUrl