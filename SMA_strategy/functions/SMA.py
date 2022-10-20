import pandas as pd

def SMA (df, n):
    # df is data for the calculation of arithmetic moving average
    # n is the time periods (in days) for the calculation average
    sma = df.rolling(window = n).mean()
    return pd.DataFrame(sma)