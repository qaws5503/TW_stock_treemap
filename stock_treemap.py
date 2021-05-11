# coding:utf-8

#%%
import pandas as pd
import numpy as np
import plotly.express as px
import web_crawler
from pandas.tseries.offsets import BDay
import datetime

def read_data():
    # check is holiday or not
    date = datetime.datetime.today()
    if date.weekday()>=5:
        date = date - BDay(1)
    # check if the data is the most newest
    if pd.read_csv("stock_data.csv",nrows=1).loc[0,'date']!=date.strftime("%Y/%m/%d"):
        web_crawler.export_data()
    stock_data = pd.read_csv("stock_data.csv")
    stock_data = stock_data.dropna(axis = 0)
    return stock_data

def run(save):
    stock_data = read_data()
    stock_data['All'] = 'All'
    fig = px.treemap(stock_data, path=['All', 'industry', 'name'],
                        values='market_value(100M)', color='change_percentage',
                        color_continuous_scale=[[0,'green'],[0.5,'lightgrey'],[1,'red']],
                        color_continuous_midpoint=0,
                        labels={
                            'change_percentage':'漲跌幅 (%)'
                        },
                        custom_data=['price',
                                    'change',
                                    'symbol',
                                    'industry'])
    # industry's customdata will have (?), because of empty. so replace it to nothing
    fig.data[0].customdata = np.where((fig.data[0].customdata=='(?)'), 'None', fig.data[0].customdata)
    # Custom hover text
    fig.data[0].hovertemplate = '<b>%{customdata[2]} %{label}</b><br><br>收盤價=%{customdata[0]}<br>市值=%{value}億<br>產業=%{customdata[3]}<br>漲跌幅=%{color:.2f}%<br>漲跌額=%{customdata[1]}<extra></extra>'
    fig.update_layout(title=stock_data.loc[0,'date']+' 台股板塊漲幅',
                        uniformtext=dict(minsize=12, mode='hide'))
    if save == True:
        fig.write_html("stock.html")
    fig.show()

# %%
