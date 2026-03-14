import requests

def get_price(symbol="BTC"):

    url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"

    data=requests.get(url).json()

    return f"💰 Prix {symbol}\n\n{data['price']} $"


def top_crypto():

    url="https://api.coingecko.com/api/v3/coins/markets"

    params={
        "vs_currency":"usd",
        "order":"market_cap_desc",
        "per_page":10,
        "page":1
    }

    data=requests.get(url,params=params).json()

    msg="🚀 Top cryptos\n\n"

    for coin in data[:5]:

        msg+=f"{coin['name']} : {coin['price_change_percentage_24h']:.2f}%\n"

    return msg


def btc_chart():

    return "📊 Graphique BTC\nhttps://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT"