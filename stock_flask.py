#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:39:00 2021

@author: apple
"""

import pandas as pd
import statistics
import numpy as np

def read_data():
    stock_data = pd.read_csv("stock_data.csv")
    stock_data = stock_data.dropna(axis = 0)
    return stock_data


def write_array(stock_data, category, category_percentage):
    array_data = np.array(['Stock', 'Parent', 'Market price (size)', 'Stock price increase/decrease (color)']
                          , dtype=object)
    array_data = np.append(array_data, np.array(["All", None, 0, 0]))
    for now_category in category:
        new = np.array([now_category, "All", int(0), float(round(category_percentage[now_category],2)*100)], dtype=object)
        array_data = np.append(array_data, new)

    for i in range(len(stock_data)):
        now = stock_data.iloc[i,:]
        new = np.array([now["name"]+" "+str(now["change_percentage"])+" %", now["market_value"], int(now["market_price(100M)"]), float(now["change_percentage"]*100)], dtype=object)
        array_data = np.append(array_data,new)
    
    return array_data


def write_html(array_data):
    html_str1 = """
    <!DOCTYPE html>
    <html>
      <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
          google.charts.load('current', {'packages':['treemap']});
          google.charts.setOnLoadCallback(drawChart);
          function drawChart() {
            var data = google.visualization.arrayToDataTable(
            """
            
    html_str2 = """
            );

            tree = new google.visualization.TreeMap(document.getElementById('chart_div'));

            tree.draw(data, {
              minColor: '#0d0',
              midColor: '#ddd',
              maxColor: '#f00',
              headerHeight: 15,
              fontColor: 'black',
              showScale: true,
              maxPostDepth: 2
            });

          }
        </script>
      </head>
      <body>
        <div id="chart_div" style="width: 1400px; height: 800px;"></div>
      </body>
    </html>
    """

    # python has no null, so use None then replace it
    html_str = html_str1 + str(array_data).replace("None","null") + html_str2

    Html_file= open("web/templates/index.html","w")
    Html_file.write(html_str)
    Html_file.close()

def run():

    stock_data = read_data()

    # get a list of category
    category = list(set(stock_data['market_value'].tolist()))

    category_percentage = {}
    for now_category in category:
        df = stock_data[stock_data['market_value']==now_category]
        category_percentage[now_category] = statistics.mean(df["change_percentage"])

    array_data = write_array(stock_data, category, category_percentage)
    array_data = array_data.reshape(-1,4).tolist() # without tolist() array can't display all value
    write_html(array_data)