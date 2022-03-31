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
    columns = ['time',
    'symbol',
    'buy',
    'sell',
    'changeRate',
    'changePrice',
    'high',
    'low',
    'vol',
    'volValue',
    'last',
    'averagePrice',
    'takerFeeRate',
    'makerFeeRate',
    'takerCoefficient',
    'makerCoefficient',])

# CSV - INCLUDE THESE COLUMNS ONLY:
df = df[["vol","averagePrice"]]

# CSV - EXPORT
df.to_csv(csv_name+'.csv', header=True, index=False)

print("Success...")