# 104人力銀行爬蟲練習

- [x] 爬取資料 
- [x] 整理成Data Frame 
- [x] 擷取Data Frame照片
- [x] 整理關鍵字及出現頻率(webCloud)

## 流程
  - 至網站以關鍵字"資料分析"抓取職缺: /Job104.py
  - 每一職缺內容以.txt存於資料夾: /104job 
  - 用pandas整理每筆職缺資料，並存成.csv: /104Job_pandas.ipynb
  - 使用文字雲找出當前職缺內容熱門關鍵字: /jiebaforContent.ipynb
 
## 心得
一開始用requests與beautiful只能爬取頁面搜尋結果資料，如果想進去頁面點開的網頁內容，Headers除了本身的User-Agent參數，需另帶Referer，回傳的結果用Json.loads開啟。  

值得注意一點:  
內容詳細在開發人員工具Network > 一串ID，這邊要去requests ID 內的url+Referer的參數，帶出需要的資料。

## 爬取結果
![image](https://github.com/newgirlcarol/webCrawler_learning/blob/master/%E6%93%B7%E5%8F%96.JPG)

## webCloud
![image](https://github.com/newgirlcarol/webCrawler_learning/blob/master/skill.jpg)
