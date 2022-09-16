# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:46:19 2022

@author: Nick
"""
import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

apple_info = apple.info # Extract info as a python dictionary
apple_info

apple_share_price_data = apple.history(period='max')    #returns a Pandas DF
apple_share_price_data.head()

apple_share_price_data.reset_indext(inplace=True)
apple_share_price_data.plot(x="Date",y="Open")

apple.dividends
apple.dividends.plot()





