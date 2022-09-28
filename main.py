from email.mime import image
import imp
import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen


# Titles and subtitles
st.title("Cryptocurrency Daily Prices")
# Defining ticker variables

Bitcoin     = 'BTC-USD'
Ethereum    = 'ETH-USD'
Ripple      = 'YRP-USD'
BitcoinCash = 'BCH-USD'



# access data from Yahoo Finance

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
YRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

# fetch history data
BTCHis = BTC_Data.history(period="max")
ETHHis = BTC_Data.history(period="max")
YRPHis = BTC_Data.history(period="max")
BCHHis = BTC_Data.history(period="max")

# fetch crypto data from table
BTC = yf.download(Bitcoin, start="2022-08-19", end="2022-08-19")
ETH = yf.download(Ethereum, start="2022-08-19", end="2022-08-19")
YRP = yf.download(Ripple, start="2022-08-19", end="2022-08-19")
BCH = yf.download(BitcoinCash, start="2022-08-19", end="2022-08-19")

# Bitcoin
st.write("BITCOIN (CHF)")
imageBTC = Image.open(urlopen('https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@bea1a9722a8c63169dcc06e86182bf2c55a76bbc/128/icon/btc.png'))
st.image(imageBTC)
# Display Image End
st.table(BTC)
st.bar_chart(BTCHis.Close)

# Ethereum
st.write("Ethereum (CHF)")
imageETH = Image.open(urlopen('https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@bea1a9722a8c63169dcc06e86182bf2c55a76bbc/128/icon/eth.png'))
st.image(imageETH)
# Display Image End
st.table(ETH)
st.bar_chart(ETHHis.Close)

# Ripple
st.write("Ripple (CHF)")
imageYRP = Image.open(urlopen('https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@bea1a9722a8c63169dcc06e86182bf2c55a76bbc/128/icon/elec.png'))
st.image(imageYRP)
# Display Image End
st.table(YRP)
st.bar_chart(YRPHis.Close)

# BitcoinCash
st.write("BitcoinCash (CHF)")
imageBCH = Image.open(urlopen('https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@bea1a9722a8c63169dcc06e86182bf2c55a76bbc/128/icon/bch.png'))
st.image(imageBCH)
# Display Image End
st.table(BCH)
st.bar_chart(BCHHis.Close)

