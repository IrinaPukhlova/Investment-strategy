## Project Description
The purpose of this work was chosen to test the performance of a green investment. And the main hypothesis is: Will green investment always bring a good return?
To test this hypothesis is used the Global X Renewable Energy Producers ETF (ticker - RNRG).

The main analysis is done in the Jupiter Notebook file SMA_strategy_analysis.ipynb

### Part 1 - Downloading and exploring data
Data were downloaded using the Pandas Datareader package from Yahoo Finance. And with the help of the Matplotlib library, a visual analysis of the Close price of the RNRG stock was done.


### Part 2 – Description and implementation of the Trading Strategy (Pair of Simple Moving Average)
Three pairs of short and long SMA were chosen to test this strategy:
- SMA30 and SMA 365
- SMA30 and SMA 90
- SMA30 and SMA 180

These three pairs were performed to test our main hypothesis, to see if the return on green investments is always positive, or if it still depends more on the right choice of strategy parameters.

2 additional functions were written to implement the strategy
- [SMA.py](https://github.com/IrinaPukhlova/Investment-strategy/blob/main/SMA_strategy/functions/SMA.py) - calculates SMA with any specified period
- [strategy_2_sma.py](https://github.com/IrinaPukhlova/Investment-strategy/blob/main/SMA_strategy/functions/strategy_2_sma.py) - it directly implements the strategy logic and generates buy and sell signals as a result

Also,  the performance was calculated for each SMA pair with 2 types: without and with reinvestment of income from the previous trade.
2 functions were written to calculate the performance of the stock:
- [performance.py](https://github.com/IrinaPukhlova/Investment-strategy/blob/main/SMA_strategy/functions/performance.py) - calculates performance without reinvestment of income from the previous trade.
- [performance_reinvest.py](https://github.com/IrinaPukhlova/Investment-strategy/blob/main/SMA_strategy/functions/performance_reinvest.py) - calculates performance with reinvestment

### Part 3 – Conclusion
Here the findings of my experiment and the main hypothesis are described, as the references that were used in the course of the study.
