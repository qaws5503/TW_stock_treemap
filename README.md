# 台股股票板塊漲幅 (treemap)

## 簡介

在台股就總計有 1730 家上市上櫃公司(2020)，此 Treemap 可以快速看出今天收盤漲幅的狀況。

## Demo

![demo](https://github.com/qaws5503/TW_stock_treemap/blob/main/demo.gif)

## 說明

Treemap 之大小為公司市值，顏色為漲幅(%)。

Treemap 為 Google Chart 所提供，說明[在此](https://developers.google.com/chart/interactive/docs/gallery/treemap)

### 架構

![structure](https://github.com/qaws5503/TW_stock_treemap/blob/main/tw_stock.png)

## 操作

### Normal using

`python3 main.py`


### For Flask

`python3 main.py -m 1`

再到`/web`內執行stock_flask.py即可架設網站
