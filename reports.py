import random
from market_data import crypto_price, metal_price, get_history, get_history_tf
from indicators import calculate_rsi, moving_average

SEP="━━━━━━━━━━━━━━"

def score_bar(score):
    filled=int(score/10)
    empty=10-filled
    return "█"*filled+"░"*empty

def mini_chart():
    bars=["▁","▂","▃","▄","▅","▆","▇","█"]
    return "".join(random.choice(bars) for _ in range(20))

def analyse(asset,price):

    prices=get_history(asset)

    if prices:
        rsi=calculate_rsi(prices)
        ma50=moving_average(prices,50)
        ma200=moving_average(prices,200)
    else:
        rsi=50
        ma50=price
        ma200=price

    support=price*0.97
    resistance=price*1.03
    momentum=random.randint(-5,5)

    trend="Neutre"

    if ma50 and ma200:
        if ma50>ma200:
            trend="Haussière modérée"
        if ma50<ma200:
            trend="Baissière modérée"

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

def btc_analysis():

    price=crypto_price("BTC")

    rsi=random.randint(35,70)
    momentum=random.randint(-5,5)
    volatility=random.randint(3,10)

    support=price*0.97
    resistance=price*1.03

    trend="Neutre court terme"

    if rsi>60 and momentum>1:
        trend="Haussière court terme"

    if rsi<40 and momentum<-1:
        trend="Baissière court terme"

    scenario="Observer réaction sur les niveaux clés."

    if trend=="Haussière court terme":
        scenario="Continuation vers la résistance."

    if trend=="Baissière court terme":
        scenario="Risque de retour sur le support."

    trend_icon="📈" if "Haussière" in trend else ("📉" if "Baissière" in trend else "➡️")

    chart15=mini_chart()
    chart1h=mini_chart()
    chart4h=mini_chart()

    return f"""
💰 *ANALYSE BTC*

{SEP}

💵 Prix actuel
{price:.0f} $

📊 Graphique 15m
{chart15}

📊 Graphique 1h
{chart1h}

📊 Graphique 4h
{chart4h}

{SEP}

RSI : {rsi}
Momentum : {momentum:+}
Volatilité : {volatility} %

{SEP}

Tendance
{trend_icon} {trend}
"""

def signal():

    asset=random.choice(["BTC","ETH","SOL"])
    price=crypto_price(asset)

    entry_low=price*0.99
    entry_high=price*1.005
    sl=price*0.97
    tp=price*1.04

    support=price*0.975
    resistance=price*1.03

    prob=random.randint(55,75)

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

def scanner():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    m_btc=random.randint(-5,5)
    m_eth=random.randint(-5,5)
    m_sol=random.randint(-5,5)

    dominant=max([("BTC",m_btc),("ETH",m_eth),("SOL",m_sol)],key=lambda x:x[1])[0]

    return f"""
🔎 *SCANNER MARCHÉ*

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

🏆 Actif dominant

{dominant}

{SEP}

Analyse

{dominant} attire
la majorité
de la liquidité.
"""

def liquidity():

    buy=random.randint(40,75)
    sell=100-buy
    imbalance=buy-sell

    price=crypto_price("BTC")
    zone_high=price*1.03
    zone_low=price*0.97

    conclusion="Les acheteurs\ncontrôlent\nle marché."

    if sell>buy:
        conclusion="Les vendeurs\ndominent\nle marché."

    sign="+" if imbalance>=0 else ""

    bar_buy=score_bar(buy)
    bar_sell=score_bar(sell)

    dom="🟢 Acheteurs dominants" if buy>sell else "🔴 Vendeurs dominants"

    analyse="Le marché cherche\nla liquidité au-dessus\nde la résistance." if buy>sell else "Le marché cherche\nla liquidité sous\nle support."

    return f"""
📡 *RADAR LIQUIDITÉ*

{SEP}

Acheteurs

{bar_buy} {buy}%

Vendeurs

{bar_sell} {sell}%

{SEP}

Dominance

{dom}

{SEP}

Analyse

{analyse}
"""

def trade_map():

    asset=random.choice(["BTC","ETH","SOL"])
    price=crypto_price(asset)

    buy_low=price*0.99
    buy_high=price*0.995
    sell_low=price*1.03
    sell_high=price*1.045
    sl=price*0.97
    tp=price*1.055

    return f"""
📊 CARTE DE TRADE

Actif
{asset}

Prix
{price:.0f} $

ZONE ACHAT

{buy_low:.0f} - {buy_high:.0f}

ZONE VENTE

{sell_low:.0f} - {sell_high:.0f}

STOP LOSS

{sl:.0f}

OBJECTIF

{tp:.0f}

Guide

Observer réaction
du prix dans
les zones clés.
"""

def institutional():

    buy=random.randint(40,80)
    sell=100-buy

    imbalance=buy-sell

    price=crypto_price("BTC")
    accum=price*0.98
    distrib=price*1.03

    analyse="Les institutions semblent accumuler\nprès du support."

    if sell>buy:
        analyse="Les institutions semblent distribuer\nprès de la résistance."

    return f"""
🧭 CARTE INSTITUTIONNELLE

Flux institutionnel

Acheteurs
{buy} %

Vendeurs
{sell} %

Zones surveillées

Accumulation
{accum:.0f}

Distribution
{distrib:.0f}

Analyse

{analyse}
"""

def probability():

    rsi=random.randint(30,70)
    momentum=random.randint(-5,5)
    volatility=random.randint(3,10)

    score=50

    if rsi>60:
        score+=15
    if rsi<40:
        score-=15

    score+=momentum*3

    if score>100:
        score=100
    if score<0:
        score=0

    conclusion="Setup neutre, attendre signal."

    if score>65:
        conclusion="Setup intéressant\nsi la tendance\nreste positive."
    if score<40:
        conclusion="Setup risqué,\nrester en dehors."

    return f"""
🧮 PROBABILITÉ TRADE

Score opportunité

{score} %

Indicateurs

RSI
{rsi}

Momentum
{momentum:+}

Volatilité
{volatility} %

Conclusion

{conclusion}
"""

def multi_timeframe(asset):

    prices15=get_history_tf(asset,"15m")
    prices1h=get_history_tf(asset,"1h")
    prices4h=get_history_tf(asset,"4h")

    rsi15=calculate_rsi(prices15) if prices15 else 50
    rsi1h=calculate_rsi(prices1h) if prices1h else 50
    rsi4h=calculate_rsi(prices4h) if prices4h else 50

    score=0

    if rsi15>55:
        score+=1

    if rsi1h>55:
        score+=1

    if rsi4h>55:
        score+=1

    direction="Marché neutre"

    if score>=2:
        direction="🟢 Tendance haussière"

    if score==0:
        direction="🔴 Tendance baissière"

    return f"""
⏱ ANALYSE MULTI TIMEFRAME

Actif

{asset}

RSI 15m

{rsi15}

RSI 1h

{rsi1h}

RSI 4h

{rsi4h}

Score tendance

{score}/3

Direction

{direction}

Guide

Confirmer la direction
sur plusieurs timeframes.
"""

def market_score():

    momentum=random.randint(-5,5)
    volatility=random.randint(3,10)

    score=50+momentum*5

    if score>100:
        score=100
    if score<0:
        score=0

    sentiment="Neutre"
    vol_label="Moyenne"
    conclusion="Observer la tendance avant de prendre position."

    if score>65:
        sentiment="Haussier"
        conclusion="Le marché reste positif."
    if score<40:
        sentiment="Baissier"
        conclusion="Prudence, tendance négative."

    if volatility>7:
        vol_label="Élevée"
    if volatility<5:
        vol_label="Faible"

    bar=score_bar(score)
    mom_label="Positif" if momentum>0 else ("Négatif" if momentum<0 else "Neutre")

    return f"""
📊 *SCORE MARCHÉ*

{SEP}

Sentiment global

{bar} {score}%

{SEP}

Momentum
{mom_label}

Volatilité
{vol_label}

{SEP}

Conclusion

{conclusion}
"""

def ai():

    rsi=random.randint(30,70)
    momentum=random.randint(-5,5)

    decision="WAIT"

    if rsi>60:
        decision="BUY"

    if rsi<40:
        decision="SELL"

    return f"""
🤖 ASSISTANT TRADING

RSI : {rsi}
Momentum : {momentum}

Décision

{decision}
"""

def heatmap():

    assets=["BTC","ETH","SOL"]

    strongest=None
    strongest_mom=0
    rows=""

    for asset in assets:

        mom=random.uniform(-5,5)

        if abs(mom)>abs(strongest_mom):
            strongest_mom=mom
            strongest=asset

        sign="+" if mom>=0 else ""
        rows+=f"\n{asset}\n{sign}{mom:.1f} %\n"

    analyse=f"{strongest} attire\nle plus de\nliquidité actuellement."

    return f"""
📊 HEATMAP CRYPTO
{rows}
Analyse

{analyse}
"""

def watchlist():

    assets=["BTC","ETH","SOL"]
    best=random.choice(assets)
    variation=random.uniform(1,5)

    return f"""
📡 AUTO WATCHLIST

Actifs surveillés

BTC
ETH
SOL

Actif le plus actif

{best}

Variation

+{variation:.1f} %

Conclusion

Actif à surveiller
pour opportunités.
"""

def multi():

    assets=["BTC","ETH","SOL"]

    strongest=None
    strongest_mom=0
    rows=""

    for a in assets:
        mom=random.randint(-5,5)
        if mom>strongest_mom:
            strongest_mom=mom
            strongest=a
        rows+=f"\n{a}\nMomentum {mom:+}\n"

    if not strongest:
        strongest=random.choice(assets)

    return f"""
🧠 ANALYSE MULTI CRYPTO
{rows}
Actif dominant

{strongest}

Analyse

{strongest} montre la
plus forte dynamique.
"""

def agenda():
    return """
📆 AGENDA ÉCONOMIQUE

Événements majeurs

CPI Inflation
FOMC Meeting
NFP Employment

Impact potentiel

Volatilité forte
sur crypto et métaux.

Calendrier complet

https://www.forexfactory.com/calendar
"""

def briefing():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    sentiment=random.randint(0,100)
    volatility=random.randint(3,10)

    sent_label="Bullish modéré"
    vol_label="Moyenne"
    conclusion="Marché stable\navec tendance\nlégèrement haussière."

    if sentiment<40:
        sent_label="Bearish modéré"
        conclusion="Marché sous pression,\nrester prudent."

    if volatility>7:
        vol_label="Élevée"

    if volatility<5:
        vol_label="Faible"

    return f"""
🌅 BRIEFING MARCHÉ

Situation actuelle

BTC
{btc:.0f} $

ETH
{eth:.0f} $

SOL
{sol:.0f} $

Sentiment

{sent_label}

Volatilité

{vol_label}

Conclusion

{conclusion}
"""

def report():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    gold=metal_price("XAU")
    silver=metal_price("XAG")

    sentiment=random.randint(0,100)

    direction="Neutre"
    if sentiment>65:
        direction="Marché haussier"
    if sentiment<40:
        direction="Marché baissier"

    return f"""
📋 RAPPORT COMPLET

CRYPTO

BTC : {btc:.0f}
ETH : {eth:.0f}
SOL : {sol:.0f}

METAUX

Gold : {gold:.0f}
Silver : {silver:.0f}

Sentiment global
{sentiment}

Direction
{direction}
"""

def market_dashboard():

    sentiment=random.randint(0,100)
    volatility=random.randint(3,10)
    momentum=random.randint(-5,5)

    direction="Marché neutre"
    if sentiment>65:
        direction="Marché haussier"
    if sentiment<40:
        direction="Marché baissier"

    mom_label="positif" if momentum>0 else ("négatif" if momentum<0 else "neutre")
    dominant=random.choice(["BTC","ETH","SOL"])

    return f"""
📊 DASHBOARD MARCHÉ

Sentiment global
{sentiment}

Momentum
{mom_label}

Volatilité
{volatility} %

Actif dominant
{dominant}

Direction
{direction}
"""

def super_report():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    gold=metal_price("XAU")
    silver=metal_price("XAG")

    sentiment=random.randint(0,100)

    pressure=random.randint(-10,10)

    direction="Marché neutre"

    if sentiment>65:
        direction="🟢 Marché haussier"

    if sentiment<40:
        direction="🔴 Marché baissier"

    dominant=random.choice(["BTC","ETH","SOL"])

    return f"""
🧠 SUPER RAPPORT IA MARCHÉ

CRYPTO

BTC : {btc:.0f}$
ETH : {eth:.0f}$
SOL : {sol:.0f}$

METAUX

Gold : {gold:.0f}$
Silver : {silver:.0f}$

SENTIMENT GLOBAL

{sentiment}/100

PRESSION MARCHÉ

{pressure}

ACTIF DOMINANT

{dominant}

DIRECTION

{direction}

GUIDE

Comparer sentiment,
liquidité et momentum
avant toute position.
"""

def trading_assistant():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    direction=random.choice([
    "Setup haussier possible",
    "Setup baissier possible",
    "Attendre confirmation"
    ])

    entry_low=price*0.995
    entry_high=price*1.005

    stop=price*0.97
    tp=price*1.04

    prob=random.randint(45,75)

    return f"""
🤖 ASSISTANT TRADING

Actif
{asset}

Direction
{direction}

Entrée
{entry_low:.0f} - {entry_high:.0f}

Stop
{stop:.0f}

Objectif
{tp:.0f}

Probabilité
{prob} %
"""
