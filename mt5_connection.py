import MetaTrader5 as mt5
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#conecta-se ao Metatrader 5

mt5.initialize()

quotes = mt5.copy_rates_from_pos("MinDolAug23",mt5.TIMEFRAME_M1,0,100)
dates = pd.to_datetime([pd.Timestamp.fromtimestamp(bar[0]) for bar in quotes])

close_prices = np.array([bar[4] for bar in quotes])

series = pd.Series(close_prices,index=dates)
series = series.dropna()
series = series.round(decimals=4)

plt.plot(series)
plt.show()
