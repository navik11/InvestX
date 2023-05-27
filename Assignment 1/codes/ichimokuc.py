# Ichimoku Cloud Lines 
import pandas as pd
import matplotlib.pyplot as plt

def calculate_tenkan_sen(high, low):
    # Conversion line
    return (high.rolling(window=9).max() + low.rolling(window=9).min()) / 2

def calculate_kijun_sen(high, low):
    # Base line
    return (high.rolling(window=26).max() + low.rolling(window=26).min()) / 2

def calculate_senkou_span_a(tenkan_sen, kijun_sen):
    # Leading Span A
    return ((tenkan_sen + kijun_sen) / 2).shift(26)

def calculate_senkou_span_b(high, low):
    # Leading Span B
    return ((high.rolling(window=52).max() + low.rolling(window=52).min()) / 2)

def calculate_chikou_span(close):
    # Lagging Span
    return close.shift(-26)

# Usage
data = pd.read_csv('TSLA.csv')  
high = data['High']
low = data['Low']
close = data['Close']
date = data['Date']

conv_line = calculate_tenkan_sen(high, low)
base_line = calculate_kijun_sen(high, low)
leadS_a = calculate_senkou_span_a(conv_line, base_line)
leadS_b = calculate_senkou_span_b(high, low)
lagS = calculate_chikou_span(close)

plt.plot(date, conv_line, label='Conversion Line (9)', color='blue', alpha=0.6, linewidth=0.7)
plt.plot(date, base_line, label='Base Line (26)', color='black', alpha=0.6, linewidth=0.7)
plt.plot(date, leadS_a, label='Leading Span A (26)', color='green', alpha=0.3, linewidth=0.7)
plt.plot(date, leadS_b, label='Leading Span B (52)', color='red', alpha=0.3, linewidth=0.7)
plt.fill_between(date, leadS_a, leadS_b, color='grey', alpha=0.15)
plt.plot(date, lagS, label='Lagging Span (-26)', color='grey', alpha=0.6, linewidth=0.6)

plt.title('Ichimoku Cloud ( TSLA in FY 2022-23 )')
plt.ylabel('Price')
plt.xlabel('Timeline (Daily)')
plt.legend(loc='best')

ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])

plt.show()