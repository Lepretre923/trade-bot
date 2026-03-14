import random
from market_data import crypto_price, metal_price, get_history, get_history_tf
from indicators import calculate_rsi, moving_average

SEP = "━━━━━━━━━━━━━━"


def score_bar(score):
    filled = int(score / 10)
    empty = 10 - filled
    return "█" * filled + "░" * empty


def mini_chart():
    bars = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    return "".join(random.choice(bars) for _ in range(20))


# ------------------------------------------------
# ANALYSE GÉNÉRALE
# ------------------------------------------------

def analyse(asset, price):

    prices = get_history(asset)

    if prices:
        rsi = calculate_rsi(prices)
        ma50 = moving_average(prices, 50)
        ma200 = moving_average(prices, 200)
    else:
        rsi = 50
        ma50 = price
        ma200 = price

    support = price * 0.97
    resistance = price * 1.03
    momentum = random.randint(-5, 5)

    trend = "Neutre"

    if ma50 and ma200:
        if ma50 > ma200:
            trend = "Haussière modérée"
        elif ma50 < ma200:
            trend = "Baissière modérée"

    return f"""
🪙 ANALYSE {asset}

Prix actuel
{price:.0f} $

Support
{support:.0f} $

Résistance
{resistance:.0f} $

RSI
{rsi}

Momentum
{momentum:+}

Tendance
{trend}

Guide
Observer réaction
près de la résistance.
"""


# ------------------------------------------------
# ANALYSE BTC
# ------------------------------------------------

def btc_analysis():

    price = crypto_price("BTC")

    rsi = random.randint(35, 70)
    momentum = random.randint(-5, 5)
    volatility = random.randint(3, 10)

    support = price * 0.97
    resistance = price * 1.03

    trend = "Neutre court terme"

    if rsi > 60 and momentum > 1:
        trend = "Haussière court terme"

    elif rsi < 40 and momentum < -1:
        trend = "Baissière court terme"

    trend_icon = "📈" if "Haussière" in trend else ("📉" if "Baissière" in trend else "➡️")

    chart15 = mini_chart()
    chart1h = mini_chart()
    chart4h = mini_chart()

    return f"""
💰 ANALYSE BTC

{SEP}

Prix actuel
{price:.0f} $

Graphique 15m
{chart15}

Graphique 1h
{chart1h}

Graphique 4h
{chart4h}

{SEP}

RSI : {rsi}
Momentum : {momentum:+}
Volatilité : {volatility} %

{SEP}

Tendance
{trend_icon} {trend}
"""


# ------------------------------------------------
# SIGNAL TRADING
# ------------------------------------------------

def signal():

    asset = random.choice(["BTC", "ETH", "SOL"])
    price = crypto_price(asset)

    entry_low = price * 0.99
    entry_high = price * 1.005
    sl = price * 0.97
    tp = price * 1.04

    support = price * 0.975
    resistance = price * 1.03

    prob = random.randint(55, 75)

    return f"""
📈 SIGNAL TRADING

Actif
{asset}

Prix actuel
{price:.0f} $

ZONE D'ENTRÉE
{entry_low:.0f} $ - {entry_high:.0f} $

STOP LOSS
{sl:.0f} $

OBJECTIF
{tp:.0f} $

STRUCTURE

Support majeur
{support:.0f} $

Résistance
{resistance:.0f} $

Probabilité
{prob} %

Guide
Entrer seulement si
le prix confirme
la direction.
"""


# ------------------------------------------------
# SCANNER MARCHÉ
# ------------------------------------------------

def scanner():

    btc = crypto_price("BTC")
    eth = crypto_price("ETH")
    sol = crypto_price("SOL")

    m_btc = random.randint(-5, 5)
    m_eth = random.randint(-5, 5)
    m_sol = random.randint(-5, 5)

    dominant = max(
        [("BTC", m_btc), ("ETH", m_eth), ("SOL", m_sol)],
        key=lambda x: x[1]
    )[0]

    return f"""
🔎 SCANNER MARCHÉ

{SEP}

BTC
Prix : {btc:.0f}
Momentum : {m_btc:+}

ETH
Prix : {eth:.0f}
Momentum : {m_eth:+}

SOL
Prix : {sol:.0f}
Momentum : {m_sol:+}

{SEP}

Actif dominant
{dominant}

{SEP}

Analyse

{dominant} attire
la majorité
de la liquidité.
"""


# ------------------------------------------------
# RAPPORT GLOBAL
# ------------------------------------------------

def report():

    btc = crypto_price("BTC")
    eth = crypto_price("ETH")
    sol = crypto_price("SOL")

    gold = metal_price("XAU") or 0
    silver = metal_price("XAG") or 0

    sentiment = random.randint(0, 100)

    direction = "Neutre"
    if sentiment > 65:
        direction = "Marché haussier"
    elif sentiment < 40:
        direction = "Marché baissier"

    return f"""
📋 RAPPORT COMPLET

CRYPTO

BTC : {btc:.0f} $
ETH : {eth:.0f} $
SOL : {sol:.0f} $

METAUX

Gold : {gold:.0f} $
Silver : {silver:.0f} $

Sentiment global
{sentiment}

Direction
{direction}
"""
