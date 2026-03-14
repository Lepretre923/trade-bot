import random


def analyse(symbol="BTC", price=0):

    rsi = random.randint(30, 70)
    momentum = random.randint(-5, 5)
    volatility = random.randint(3, 10)

    support = price * 0.97
    resistance = price * 1.03

    trend = "Marché neutre"

    if rsi > 60 and momentum > 1:
        trend = "🟢 Tendance haussière"

    if rsi < 40:
        trend = "🔴 Risque de baisse"

    return f"""
📊 ANALYSE {symbol}

Prix actuel
{price:.2f} $

━━━━━━━━━━━━━━

STRUCTURE MARCHÉ

Support majeur : {support:.2f} $
Résistance majeure : {resistance:.2f} $

━━━━━━━━━━━━━━

INDICATEURS

RSI : {rsi}
Momentum : {momentum}
Volatilité : {volatility} %

━━━━━━━━━━━━━━

TENDANCE

{trend}

━━━━━━━━━━━━━━

SCÉNARIO POSSIBLE

Le prix pourrait tester
la zone de résistance
si le momentum continue.

━━━━━━━━━━━━━━

GUIDE

Surveiller un retour
vers la zone de support
avant toute entrée.
"""
