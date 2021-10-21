**標題**

    # h1 大標題 
    ## h2 次標題
    ### h3 次小標題
    ###### h6 最小標題
> # h1 大標題
> ## h2 次標題
> ###### h6 最小標題
**字體**

    *斜體* 或 _斜體_
    **粗體** 或 __粗體__
    **粗體 _斜體_** 結合重點
    ~~刪除線~~
> *斜體* \
> **粗體** \
> **粗體 _斜體_** \
> ~~刪除線~~ 
    
**斷行**

    行末 空格加反斜線 \
**區塊**

    > 第一階
    >> 第二階
    `小區塊` (字句前後加上反向引號)
    
    ```
    大區塊；或是前面空四格空白鍵
    ```
> 第一階
>> 第二階

>`小區塊`
> ```
> 大區塊
> ```
**列表**

    1. 第一個列表項目
    2. 第二個列表項目
      1. 有序次子列表(tab縮排後給數字)
    * 無序列表項目
> 1. 第一個列表項目
> 2. 第二個列表項目  
>     1. 有序次子列表
> * 無序列表項目 

**checkbox**

    - [x] 完成事項
    - [ ] 代辦事項  
> - [x] 完成事項 
> - [ ] 代辦事項

**表格**
  
    | Tables        | Are           | Cool  |
    | ------------- |:-------------:| -----:|
    | 靠左對齊       | 冒號兩邊置中對齊 | 冒號右邊靠右對齊 |
    | test        | test     | test |
> | Tables        | Are           | Cool  |
> | ------------- |:-------------:| -----:|
> | 靠左對齊       | 冒號兩邊置中對齊 | 冒號右邊靠右對齊 |
> | test        | test     | test |

**連結**

    * 連結兩邊加上`<` `>`就會產生超連結
      <http://dillinger.io/>  
    
	* 名稱兩邊加上`[` `]`然後再連結兩邊加上`(` `)`就可以將連結替換成文字連結
    [Dillinger](http://dillinger.io/ "link")
	
    * 將`[` `]`前+`!`，則可以產生圖片 (把滑鼠指向圖片可以看到註解）
    ![圖片參考名稱](https://raw.githubusercontent.com/adam-p/markdown-here/master/src/common/images/icon48.png "Logo")
> 連結兩邊加上`<` `>`就會產生超連結 <http://dillinger.io/> \
> 名稱兩邊加上`[` `]`然後再連結兩邊加上`(` `)`就可以將連結替換成文字連結  
    [Dillinger](http://dillinger.io/ "link") \
> 將`[` `]`前+`!`，則可以產生圖片 (把滑鼠指向圖片可以看到註解）
    ![圖片參考名稱](https://raw.githubusercontent.com/adam-p/markdown-here/master/src/common/images/icon48.png "Logo")

**程式碼與語法高亮**
    
    ```javascript
    var s = "JavaScript 語法高亮";
    alert(s);
    ```
    ```php
    $s = "PHP 語法高亮";
    echo $s;
    ```
> ```javascript
> var s = "JavaScript 語法高亮";
> alert(s);
> ```
> ```php
> $s = "PHP 語法高亮";
> echo $s;
> ```
