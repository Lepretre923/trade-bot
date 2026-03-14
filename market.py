import requests


# PRIX D'UNE CRYPTO
def get_price(symbol="BTC"):

    try:

        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"

        data = requests.get(url).json()

        price = float(data["price"])

        return f"""
💰 PRIX {symbol}

Prix actuel

{price:.2f} $

Source
Binance Spot
"""

    except:

        return "Erreur récupération prix marché"


# TOP CRYPTOS
def top_crypto():

    try:

        url = "https://api.coingecko.com/api/v3/coins/markets"

        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 10,
            "page": 1
        }

        data = requests.get(url, params=params).json()

        msg = "🚀 TOP CRYPTOS MARCHÉ\n\n"

        for coin in data[:5]:

            name = coin["name"]
            change = coin["price_change_percentage_24h"]

            direction = "🟢" if change > 0 else "🔴"

            msg += f"{direction} {name}  {change:.2f}%\n"

        msg += "\nAnalyse\n"
        msg += "Comparer la performance\n"
        msg += "des leaders du marché."

        return msg

    except:

        return "Erreur récupération données marché"


# GRAPH BTC
def btc_chart():

    return """
📊 GRAPHIQUE BTC

Voir analyse technique

https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT
"""
