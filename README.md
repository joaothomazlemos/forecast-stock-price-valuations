# predict-stock-price-valuations

Task intro:

We are a portfolio investment company and we make investments in the emerging markets around the world. Our company profits by investing in profitable companies, buying, holding and selling company stocks based on value investing principles.

Our goal is to establish a robust intelligent system to aid our value investing efforts using stock market data. We make investment decisions and based on intrinsic value of companies and do not trade on the basis of daily market volatility. Our profit realization strategy typically involves weekly, monthly and quarterly performance of stocks we buy or hold.

Data Description:

You are given a set of portfolio companies trading data from emerging markets including 2020 Q1-Q2-Q3-Q4 2021 Q1 stock prices. Each company stock is provided in different sheets. Each market's operating days varies based on the country of the company and the market the stocks are exchanged. Use only 2020 data and predict with 2021 Q1 data.

Data: yahoo finace data

Goal(s):

Predict stock price valuations on a 5 day basis. Recommend BUY, HOLD, SELL decisions. Maximize capital returns, minimize losses. Ideally a loss should never happen. Minimize HOLD period.

Success Metrics:

Evaluate on the basis of capital returns. Use Bollinger Bands to measure your systems effectiveness.

TOP 10 ALGORITHMS FOR FORECASTING Autoregressive (AR)

Autoregressive Integrated Moving Average (ARIMA)

Seasonal Autoregressive Integrated Moving Average (SARIMA)

Exponential Smoothing (ES)

XGBoost

Prophet

LSTM (Deep Learning)

DeepAR

N-BEATS

Temporal Fusion Transformer (Google)

1,2,3,4,6,7 algorithms are based on statistical methods, 5,8,9,10 are based on machine learning and deep learning methods.

We will test the best among the statistical algos as well as the prophet and LSTM deep learning models
Models to test against yahoo finance data (MST):

ARIMA
SARIMA
Exponential Smoothing
Prophet from facebook
LSTM
