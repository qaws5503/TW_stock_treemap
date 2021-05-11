# coding:utf-8

#%%
import stock_treemap
import stock_flask
from argparse import ArgumentParser
# %%
parser = ArgumentParser()
parser.add_argument("-m", "--mode", help="select mode, default=0. Using Flask just set to 1.", default=0)
parser.add_argument("-s", "--save", help="save as html or not, default=0. If you want to save html files set to 1.", default=0)
args = parser.parse_args()
if args.mode == 0:
    save_html = bool(args.save)
    stock_treemap.run(save_html)
if args.mode == 1:
    stock_flask.run()
# %%
