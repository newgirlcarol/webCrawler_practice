import requests
import time
import os
import json
import re

if not os.path.exists('./104job'):
    os.mkdir('./104job')

ss = requests.session()

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
          'Referer':'https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword=%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90&expansionType=job&area=6001001000&order=15&asc=0&page=2&mode=s&jobsource=2018indexpoc'}

for i in range(1, 11):
    url = 'https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword=%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90&expansionType=job&area=6001001000&order=15&asc=0&page={}&mode=s&jobsource=2018indexpoc'.format(i)
    res_search = ss.get(url, headers = headers)
    job_infos = json.loads(res_search.text)

    # Get job information from search page
    for elem in job_infos['data']['list']:
        jobLink = str(elem['link']['job'].split('//')[1])
        # Get job ID to request the new url
        jobURL_origin = elem['link']['job'].split('//')[1]
        jobID = re.findall('[5-9].+\?', jobURL_origin)

        for i in jobID:
            jobURL_new = 'https://www.104.com.tw/job/ajax/content/{}'.format(i.split('?')[0])
            headers_url = {
                'Referer': 'https://www.104.com.tw/job/{}'.format(i.split('?')[0])}
            res_url = requests.get(jobURL_new, headers = headers_url)
            job_infoDetail= json.loads(res_url.text) # output: dict

            job_Name = ''
            job_Company = ''
            jobAnnounDate = ''
            job_Detail = ''
            job_skill = ''

            try:
                job_Name= job_infoDetail['data']['header']['jobName']
                job_Company = job_infoDetail['data']['header']['custName']
                jobAnnounDate = job_infoDetail['data']['header']['appearDate']
                job_Detail = job_infoDetail['data']['jobDetail']['jobDescription']
                jobspecial = job_infoDetail['data']['condition']['specialty']
                job_skill = [x['description'] for x in jobspecial]
            except KeyError:
                continue


            article = '徵才名稱:{}\n'.format(job_Name)
            article += '徵才公司:{}\n'.format(job_Company)
            article += '徵才日期:{}\n'.format(jobAnnounDate)
            article += '其他條件:{}\n'.format(job_skill)
            article += '徵才網址:{}\n'.format(jobLink)
            article += '工作內容:{}'.format(job_Detail)



            # print(article)



            try:
                with open('./104job/{}.txt'.format(job_Name), 'w', encoding= 'utf-8') as w:
                    w.write(article)
            except FileNotFoundError:
                job_Name = job_Name.replace('/', '-')
                with open('./104job/{}.txt'.format(job_Name), 'w', encoding= 'utf-8') as w:
                    w.write(article)
            except OSError:
                continue
        time.sleep(6)

    print('=== Next Page===\n')