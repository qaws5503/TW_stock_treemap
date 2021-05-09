#%%
import requests
import bs4
import pandas as pd
import random
import time
import datetime

# 爬一次網頁
def web_crawler(rank):
    
    url = "https://goodinfo.tw/StockInfo/StockList.asp?MARKET_CAT=%E7%86%B1%E9%96%80%E6%8E%92%E8%A1%8C&INDUSTRY_CAT=%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%E6%9C%80%E9%AB%98%40%40%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%40%40%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%E6%9C%80%E9%AB%98&SHEET=%E5%85%AC%E5%8F%B8%E5%9F%BA%E6%9C%AC%E8%B3%87%E6%96%99"
    
    # 標頭檔從檢查 -> Network -> 搜尋網頁中的字 -> 點選往下找到 user-agent
    headers = {
        'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        }
    
    # GET Methond
    if rank==0:
        res = requests.get(url, headers = headers)
    # POST Methond
    else:
        data = {
            'RANK':rank
            }
        res = requests.get(url, headers = headers, data = data)
    res.encoding = 'utf-8'
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # '#' means id
    data = soup.select_one("#divStockList")
    
    dfs = pd.read_html(data.prettify())
    df = dfs[0]
    
    # 因goodinfo的表格為四格組成 要更改欄位名稱
    df.columns = df.columns.get_level_values(3)
    
    return df


def get_all_data():
    for i in range(6):
        df_now = web_crawler(str(i))
        
        if i == 0:
            df = df_now
        else:
            df = df.append(df_now, ignore_index=True)
        
        time.sleep(random.randint(2,5))
        
    return df


def export_data():
    df = get_all_data()
    # 取得想觀察的資料
    df_use = df.loc[:,['代號', '名稱','成交', '漲跌  價', '漲跌  幅', '市值  (億)', '產業別', "股價  日期"]]
    df_use = df_use.rename(columns={
                            '代號':'symbol',
                            '名稱':'name',
                            '成交':'price',
                            '漲跌  價':'change',
                            '漲跌  幅':'change_percentage',
                            '市值  (億)':'market_value(100M)',
                            '產業別':'industry',
                            '股價  日期':'date'})
    df_use['date'] = str(datetime.datetime.now().year)+'/'+df_use['date']
    df_use.to_csv('stock_data.csv', index=False)

# %%
