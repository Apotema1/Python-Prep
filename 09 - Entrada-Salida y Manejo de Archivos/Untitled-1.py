//how to get the stock data of in python? 
import yfinance as yf
# Get the data of the stock AAPL
data = yf.download('AAPL','2016-01-01','2019-08-01')


# Import the quandl package
import quandl
# Get the data from quandl
data = quandl.get("WIKI/KO", start_date="2016-01-01", end_date="2018-01-01", 
    api_key=<Your_API_Key>)





