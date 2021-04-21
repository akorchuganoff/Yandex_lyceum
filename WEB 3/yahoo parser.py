import yfinance as yf

BELU = yf.Ticker('BELU.ME')

# get stock info
print(BELU.info)

for k, v in BELU.info.items():
    if 'price' in str(k).lower():
        print(k, v)

# get historical market data
hist = BELU.history(period="5d")