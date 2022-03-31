import requests
import pandas as pd

# KUCOIN API
api_url = "https://api.kucoin.com"
csv_name = "kucoin24hrStats"

pair = "BTC-USDT"
kuStatParams = {
    "symbol":pair,
    }

# API CALL
KuStats = requests.get(f"{api_url}/api/v1/market/stats",
    params = kuStatParams,
    headers = {"content-type":"application/json"})

# DATA FRAME 
df = pd.DataFrame(KuStats.json()["data"], index=[0],
    columns = ['time', # timestamp
    'symbol', # symbol
    'buy', # best bid price
    'sell', # best ask price
    'changeRate', # 24hr change rate
    'changePrice', # 24hr change price
    'high', # Highest price in 24hr
    'low', # Lowest price in 24hr
    'vol', # 24h volume, executed based on base currency
    'volValue', # 24h traded amount
    'last', # Last traded price
    'averagePrice', # Average trading price in the last 24 hours
    'takerFeeRate', # Basic Taker Fee
    'makerFeeRate', # Basic Maker Fee
    'takerCoefficient', # Takeer Fee Coefficient
    'makerCoefficient',]) # Maker Fee Coefficient

# CSV - INCLUDE THESE COLUMNS ONLY:
df = df[["vol","averagePrice"]]

# CSV - EXPORT
df.to_csv(csv_name+'.csv', header=True, index=False)

print("Success...")