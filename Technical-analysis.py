from nsepython import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pandas_ta as ta
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Prompt the user for input
user_input = input("Enter a scrip name: ")

# Print the input string
print("You entered:", user_input)

# Define the stock symbol and timeframe
# symbol = 'RELIANCE.NS'
symbol = user_input + '.NS'
end_date = datetime.today()
start_date = end_date - timedelta(days=120)  # 4 months before today

# Fetch stock data using yfinance
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Calculate technical indicators using pandas-ta
stock_data.ta.macd(append=True)
stock_data.ta.rsi(append=True)
stock_data.ta.bbands(append=True)
stock_data.ta.obv(append=True)

# Calculate additional technical indicators
stock_data.ta.sma(length=20, append=True)
stock_data.ta.ema(length=50, append=True)
stock_data.ta.stoch(append=True)
stock_data.ta.adx(append=True)

# Calculate other indicators
stock_data.ta.willr(append=True)
stock_data.ta.cmf(append=True)
stock_data.ta.psar(append=True)

#convert OBV to million
stock_data['OBV_in_million'] =  stock_data['OBV']/1e7
stock_data['MACD_histogram_12_26_9'] =  stock_data['MACDh_12_26_9'] # not to confuse chatGTP

# Summarize technical indicators for the last day
last_day_summary = stock_data.iloc[-1][['Adj Close',
                                        'MACD_12_26_9','MACD_histogram_12_26_9', 'RSI_14', 'BBL_5_2.0', 'BBM_5_2.0', 'BBU_5_2.0','SMA_20', 'EMA_50','OBV_in_million', 'STOCHk_14_3_3',
                                        'STOCHd_14_3_3', 'ADX_14',  'WILLR_14', 'CMF_20',
                                        'PSARl_0.02_0.2', 'PSARs_0.02_0.2'
                                        ]]

print("Summary of Technical Indicators for the Last Day:")
print(last_day_summary)

# Plot the technical indicators
plt.figure(figsize=(14, 8))

# Price Trend Chart
plt.subplot(3, 3, 1)
plt.plot(stock_data.index, stock_data['Adj Close'], label='Adj Close', color='blue')
plt.plot(stock_data.index, stock_data['EMA_50'], label='EMA 50', color='green')
plt.plot(stock_data.index, stock_data['SMA_20'], label='SMA_20', color='orange')
plt.title("Price Trend")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size
plt.legend()

# On-Balance Volume Chart
plt.subplot(3, 3, 2)
plt.plot(stock_data['OBV'], label='On-Balance Volume')
plt.title('On-Balance Volume (OBV) Indicator')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size
plt.legend()

# MACD Plot
plt.subplot(3, 3, 3)
plt.plot(stock_data['MACD_12_26_9'], label='MACD')
plt.plot(stock_data['MACDh_12_26_9'], label='MACD Histogram')
plt.title('MACD Indicator')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size
plt.title("MACD")
plt.legend()

# RSI Plot
plt.subplot(3, 3, 4)
plt.plot(stock_data['RSI_14'], label='RSI')
plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size
plt.title('RSI Indicator')

# Bollinger Bands Plot
plt.subplot(3, 3, 5)
plt.plot(stock_data.index, stock_data['BBU_5_2.0'], label='Upper BB')
plt.plot(stock_data.index, stock_data['BBM_5_2.0'], label='Middle BB')
plt.plot(stock_data.index, stock_data['BBL_5_2.0'], label='Lower BB')
plt.plot(stock_data.index, stock_data['Adj Close'], label='Adj Close', color='brown')
plt.title("Bollinger Bands")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size
plt.legend()

# Stochastic Oscillator Plot
plt.subplot(3, 3, 6)
plt.plot(stock_data.index, stock_data['STOCHk_14_3_3'], label='Stoch %K')
plt.plot(stock_data.index, stock_data['STOCHd_14_3_3'], label='Stoch %D')
plt.title("Stochastic Oscillator")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size
plt.legend()

# Williams %R Plot
plt.subplot(3, 3, 7)
plt.plot(stock_data.index, stock_data['WILLR_14'])
plt.title("Williams %R")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size

# ADX Plot
plt.subplot(3, 3, 8)
plt.plot(stock_data.index, stock_data['ADX_14'])
plt.title("Average Directional Index (ADX)")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size

# CMF Plot
plt.subplot(3, 3, 9)
plt.plot(stock_data.index, stock_data['CMF_20'])
plt.title("Chaikin Money Flow (CMF)")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))  # Format date as "Jun14"
plt.xticks(rotation=45, fontsize=8)  # Adjust font size

# Show the plots
plt.tight_layout()
plt.show()

## Work on the prompt
sys_prompt = """
Assume the role as a leading Technical Analysis (TA) expert in the stock market, \
a modern counterpart to Charles Dow, John Bollinger, and Alan Andrews. \
Your mastery encompasses both stock fundamentals and intricate technical indicators. \
You possess the ability to decode complex market dynamics, \
providing clear insights and recommendations backed by a thorough understanding of interrelated factors. \
Your expertise extends to practical tools like the pandas_ta module, \
allowing you to navigate data intricacies with ease. \
As a TA authority, your role is to decipher market trends, make informed predictions, and offer valuable perspectives.

given {} TA data as below on the last trading day, what will be the next 15 days possible stock price movement? 

Summary of Technical Indicators for the Last Day:
{}""".format(symbol,last_day_summary)


print('ChatGPT prompt follows..............')
print(sys_prompt)