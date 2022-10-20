import numpy as np
import pandas as pd

def strategy_2_sma(df, short, long):
    buy_signal = []
    sell_signal = []
    #position is indicator of last deal. If = 1, it means in last trade we bought stocks. If =-1, it means we sold. If 0, there was no deal
    position = 0
    
    # cycle for identifying buy or sell signals
    for i in range (len(df)):
        # buy signals
        if df[f'SMA_{short}'][i] > df[f'SMA_{long}'][i]:
            if position != 1:
                buy_signal.append(df['Close'][i])
                sell_signal.append(np.nan)
                position = 1
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        
        # sell signals
        elif df[f'SMA_{short}'][i] < df[f'SMA_{long}'][i]:
            if position != -1:
                sell_signal.append(df['Close'][i])
                buy_signal.append(np.nan)
                position = -1
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)
        
    df['Buy signal'] = buy_signal
    df['Sell signal'] = sell_signal
    return (df)