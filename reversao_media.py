import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import MetaTrader5 as mt5


mt5.initialize()

def calcular_EMA(data,period):
    ema = []
    multiplier = 2/(period + 1)
    ema.append(data[0])

    for i in range(1,len(data)):
        ema_value = (data[i] - ema[i-1]) * multiplier + ema[i-1]
        ema.append(ema_value)

    return ema


symbol  = "MinDolAug23"
rates = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_M1,0,1620)
close_prices = np.array([bar[3] for bar in rates])
close_prices = np.divide(close_prices,1000)
close_prices = np.round(close_prices,decimals=4)

ema = calcular_EMA(close_prices,20)
ema = np.round(ema,decimals=4)

price_diff = close_prices - ema

sma_period = 20
sma_price_diff = np.convolve(price_diff,np.ones(sma_period)/sma_period,mode='valid')
sma_price_diff = np.concatenate((np.full(sma_period - 1,np.nan),sma_price_diff))

series_length = range(0,len(price_diff))

plt.plot(series_length,price_diff*1000)
plt.plot(series_length,sma_price_diff*1000,label='SMA 20')
plt.axhline(np.mean(price_diff)*1000,color="red",linestyle="--",label="média")
plt.axhline((np.mean(price_diff) + np.std(price_diff))*1000,color="green",linestyle="--",label="desvio padrão1")
plt.axhline((np.mean(price_diff) - np.std(price_diff))*1000,color="green",linestyle="--",label="desvio padrão1")
plt.axhline((np.mean(price_diff) + 2*np.std(price_diff))*1000,color="green",linestyle="--",label="desvio padrão2")
plt.axhline((np.mean(price_diff) - 2*np.std(price_diff))*1000,color="green",linestyle="--",label="desvio padrão2")
plt.show()