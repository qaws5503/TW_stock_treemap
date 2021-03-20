# 台股股票板塊漲幅 (treemap)

## 簡介

在台股就總計有 1730 家上市上櫃公司(2020)，此 Treemap 可以快速看出今天收盤漲幅的狀況。

## Demo

![demo](https://github.com/qaws5503/TW_stock_treemap/blob/main/demo.gif)

## 說明

Treemap 之大小為公司市值，顏色為漲幅(%)。

Treemap 為 Google Chart 所提供，說明[在此](https://developers.google.com/chart/interactive/docs/gallery/treemap)

![structure](https://github.com/qaws5503/TW_stock_treemap/blob/main/tw_stock.png)

### 操作

先執行 Market_price.py -> 產生stock_data.csv -> 再執行stock.py -> 自動更改web/templates/index.html -> 執行stock_flask.py即可架設網站
