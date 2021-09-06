# 104人力銀行爬蟲練習

- [x] 爬取資料 
- [x] 整理成Data Frame 
- [x] 擷取Data Frame照片
- [x] 整理關鍵字及出現頻率(webCloud)

## 心得
一開始用requests與beautiful只能爬取頁面搜尋結果資料，如果想進去頁面點開的網頁內容，Headers除了本身的User-Agent參數，需另帶Referer，回傳的結果用Json.loads開啟。  

值得注意一點:  
內容詳細在開發人員工具Network > 一串ID，這邊要去requests ID 內的url+Referer的參數，帶出需要的資料。

## 爬取結果
![image](https://github.com/newgirlcarol/webCrawler_learning/blob/master/%E6%93%B7%E5%8F%96.JPG)

## webCloud
![image](https://github.com/newgirlcarol/webCrawler_learning/blob/master/skill.jpg)
