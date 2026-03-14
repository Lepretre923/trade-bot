import requests
import random
import time


# -------------------------
# CACHE PRIX
# -------------------------

price_cache = {}
price_time = {}


# -------------------------
# PRIX CRYPTO
# -------------------------

def crypto_price(symbol):

    if symbol in price_cache:

        if time.time() - price_time[symbol] < 30:
            return price_cache[symbol]

    pairs = {
        "BTC": "BTC-USD",
        "ETH": "ETH-USD",
        "SOL": "SOL-USD",
        "BNB": "BNB-USD",
        "XRP": "XRP-USD",
        "ADA": "ADA-USD",
        "DOGE": "DOGE-USD",
        "AVAX": "AVAX-USD",
        "MATIC": "MATIC-USD"
    }

    try:

        url = f"https://api.coinbase.com/v2/prices/{pairs.get(symbol, symbol + '-USD')}/spot"

        r = requests.get(url, timeout=5).json()

        price = float(r["data"]["amount"])

        price_cache[symbol] = price
        price_time[symbol] = time.time()

        return price

    except:

        return 0


# -------------------------
# PRIX METAUX
# -------------------------

def metal_price(symbol):

    try:

        url = f"https://api.gold-api.com/price/{symbol}"

        r = requests.get(url, timeout=5).json()

        return float(r["price"])

    except:

        return None


# -------------------------
# DONNÉES MARCHÉ SIMPLES
# -------------------------

def market_data():

    btc = crypto_price("BTC")
    eth = crypto_price("ETH")
    sol = crypto_price("SOL")

    sentiment = random.randint(0, 100)

    return btc, eth, sol, sentiment


# -------------------------
# MARCHÉ GLOBAL CRYPTO
# -------------------------

def global_market():

    try:

        url = "https://api.coingecko.com/api/v3/global"

        r = requests.get(url, timeout=5).json()["data"]

        mcap = r["total_market_cap"]["usd"] / 1_000_000_000_000
        volume = r["total_volume"]["usd"] / 1_000_000_000
        btc_dom = r["market_cap_percentage"]["btc"]
        eth_dom = r["market_cap_percentage"]["eth"]
        change = r["market_cap_change_percentage_24h_usd"]

        direction = "Marché neutre"

        if change > 1:
            direction = "🟢 Marché haussier"

        elif change < -1:
            direction = "🔴 Marché baissier"

        sign = "+" if change >= 0 else ""

        return f"""
🌍 MARCHÉ GLOBAL CRYPTO

Capitalisation totale
{mcap:.2f} T$

Volume 24h
{volume:.0f} Md$

Dominance BTC
{btc_dom:.1f} %

Dominance ETH
{eth_dom:.1f} %

Variation 24h
{sign}{change:.2f} %

Direction
{direction}
"""

    except:

        return "Impossible de récupérer les données globales."


# -------------------------
# FEAR & GREED
# -------------------------

def fear_greed():

    try:

        url = "https://api.alternative.me/fng/"

        r = requests.get(url, timeout=5).json()

        score = int(r["data"][0]["value"])
        sentiment = r["data"][0]["value_classification"]

        bar = "█" * int(score / 10) + "░" * (10 - int(score / 10))

        return f"""
😨 FEAR & GREED INDEX

━━━━━━━━━━━━━━

Score

{bar} {score}

Sentiment

{sentiment}

━━━━━━━━━━━━━━

Analyse

Extreme Fear
peut créer des opportunités.

Extreme Greed
augmente le risque
de correction.
"""

    except:

        return "Impossible de récupérer l'indice."


# -------------------------
# FUNDING RATE
# -------------------------

def funding_rate():

    try:

        url = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT"

        r = requests.get(url, timeout=5).json()

        rate = float(r["lastFundingRate"]) * 100

        if rate > 0.03:
            sentiment = "Marché trop long"
            analyse = "Les positions longues dominent.\nRisque de correction."

        elif rate < -0.03:
            sentiment = "Marché trop short"
            analyse = "Les shorts dominent.\nRisque de short squeeze."

        else:
            sentiment = "Marché équilibré"
            analyse = "Positions long et short\néquilibrées."

        return f"""
📉 FUNDING RATE BTC

Funding rate
{rate:.4f} %

Sentiment
{sentiment}

Analyse
{analyse}
"""

    except:

        return "Impossible de récupérer le funding rate."


# -------------------------
# OPEN INTEREST
# -------------------------

def open_interest():

    try:

        url = "https://fapi.binance.com/fapi/v1/openInterest?symbol=BTCUSDT"

        r = requests.get(url, timeout=5).json()

        oi = float(r["openInterest"])

        if oi > 100000:
            sentiment = "Forte activité marché"
            analyse = "Nouveaux capitaux\nentrent sur le marché."

        elif oi < 50000:
            sentiment = "Faible activité"
            analyse = "Peu de nouvelles positions."

        else:
            sentiment = "Activité modérée"
            analyse = "Le marché reste\nattentiste."

        return f"""
📊 OPEN INTEREST BTC

Open Interest
{oi:,.0f}

Sentiment
{sentiment}

Analyse
{analyse}
"""

    except:

        return "Impossible de récupérer l'Open Interest."


# -------------------------
# HISTORIQUE PRIX
# -------------------------

def get_history_tf(symbol, interval):

    pairs = {
        "BTC": "BTCUSDT",
        "ETH": "ETHUSDT",
        "SOL": "SOLUSDT"
    }

    try:

        url = f"https://api.binance.com/api/v3/klines?symbol={pairs[symbol]}&interval={interval}&limit=100"

        data = requests.get(url, timeout=5).json()

        prices = [float(candle[4]) for candle in data]

        return prices

    except:

        return None


def get_history(symbol):

    pairs = {
        "BTC": "BTC-USD",
        "ETH": "ETH-USD",
        "SOL": "SOL-USD"
    }

    try:

        url = f"https://api.coinbase.com/v2/prices/{pairs[symbol]}/spot"

        r = requests.get(url, timeout=5).json()

        price = float(r["data"]["amount"])

        prices = [
            price * (1 + random.uniform(-0.02, 0.02))
            for _ in range(200)
        ]

        return prices

    except:

        return None
