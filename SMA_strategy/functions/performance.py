import math

def performance(df, invest):
    sum = 0
    subtotal = 0
    
    for i in range (1, len(df), 2):
        row = i+1
        if row <= len(df):
            if math.isnan(df['Buy signal'][i]):
                n_stocks = int(invest/df['Buy signal'][i-1])
                subtotal = (df['Sell signal'][i] - df['Buy signal'][i-1])*n_stocks
                sum += subtotal
                subtotal = 0
                n_stocks = 0
            elif not math.isnan(df['Buy signal'][i]):
                n_stocks = int(invest/df['Buy signal'][i])
                subtotal = (df['Sell signal'][i+1] - df['Buy signal'][i])*n_stocks
                sum += subtotal
                subtotal = 0
                n_stocks = 0
    return sum