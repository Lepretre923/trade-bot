import random
from market_data import crypto_price, metal_price, get_history_tf

SEP="━━━━━━━━━━━━━━"

SCAN_ASSETS=[
    "BTC","ETH","SOL","BNB","XRP",
    "ADA","DOGE","AVAX","MATIC"
]

# ------------------------------------------------
# SCANNER OPPORTUNITÉS
# ------------------------------------------------

def market_opportunity_scanner():

    results=[]

    for asset in SCAN_ASSETS:

        price=crypto_price(asset)

        rsi=random.randint(30,70)
        momentum=random.randint(-5,5)

        score=50+momentum*5

        if rsi>60:
            score+=10
        if rsi<40:
            score-=10

        results.append((asset,score,price))

    results=sorted(results,key=lambda x:x[1],reverse=True)

    message=f"🚀 SCANNER OPPORTUNITÉS\n\n{SEP}\n"

    for asset,score,price in results[:5]:

        message+=f"""
{asset}

Prix : {price:.0f}$
Score : {score}/100

{SEP}
"""

    message+="\nGuide\nSurveiller les actifs avec le score le plus élevé."

    return message


# ------------------------------------------------
# SCORE GLOBAL MARCHÉ
# ------------------------------------------------

def market_direction_score():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    btc_m=random.randint(-5,5)
    eth_m=random.randint(-5,5)
    sol_m=random.randint(-5,5)

    score=50+(btc_m+eth_m+sol_m)*3

    if score>100:
        score=100
    if score<0:
        score=0

    direction="Marché neutre"

    if score>65:
        direction="🟢 Marché haussier"

    if score<40:
        direction="🔴 Marché baissier"

    return f"""
📊 SCORE GLOBAL MARCHÉ

BTC : {btc:.0f}$
ETH : {eth:.0f}$
SOL : {sol:.0f}$

Score global
{score}/100

Direction
{direction}

Guide
Comparer momentum
et sentiment global
avant toute position.
"""


# ------------------------------------------------
# SMART MONEY RADAR
# ------------------------------------------------

def smart_money_radar():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    liquidity_high=price*1.03
    liquidity_low=price*0.97

    pattern=random.choice([
        "Possible stop hunt",
        "Possible fake breakout",
        "Accumulation institutionnelle",
        "Distribution institutionnelle"
    ])

    probability=random.randint(30,90)

    return f"""
🧠 SMART MONEY RADAR

Actif
{asset}

Prix
{price:.0f}$

Liquidité haute
{liquidity_high:.0f}$

Liquidité basse
{liquidity_low:.0f}$

Pattern détecté
{pattern}

Probabilité
{probability} %

Guide
Le marché cherche
souvent les zones
de liquidité avant
un mouvement fort.
"""
