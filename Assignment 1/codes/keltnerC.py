import pandas as pd
import yfinance as yf

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def calculate_ema(dataframe):
    ema = dataframe['Close'].ewm(span=20, adjust=False).mean()
    return ema

def calculate_atr(data):
    # Calculate the True Range (TR)
    data['HL'] = data['High'] - data['Low']
    data['HC'] = abs(data['High'] - data['Close'].shift(1))
    data['LC'] = abs(data['Low'] - data['Close'].shift(1))
    data['TR'] = data[['HL', 'HC', 'LC']].max(axis=1)

    # Calculate the Average True Range (ATR)
    # I choose 15 period
    data['ATR'] = data['TR'].rolling(15).mean()

    return data['ATR']


data = pd.read_csv('TSLA.csv')

date = data['Date']
ema = calculate_ema(data)
atr = calculate_atr(data)
# print(ema)
plt.plot(date, ema, color='grey', linewidth=0.9, alpha=0.8, label='20 Period EMA')
plt.plot(date, ema-(2*atr), color='grey', linewidth=0.8, alpha=0.6)
plt.plot(date, ema+(2*atr), color='grey', linewidth=0.8, alpha=0.6)
plt.fill_between(date, ema-(2*atr), ema+(2*atr), color='grey', alpha=0.15)

plt.title('Keltner Channels ( TSLA in FY 2022-23 )')
plt.ylabel('Price')
plt.xlabel('Timeline (Daily)')
plt.plot([], [], ' ', label='15 Period ATR')
plt.plot([], [], ' ', label='2x ATR Multiplier')
plt.legend(loc='best')

ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])

plt.show()
