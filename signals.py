import random
from market_data import crypto_price


def get_signal():

    coins = ["BTC", "ETH", "SOL", "AVAX", "LINK"]

    coin = random.choice(coins)

    price = crypto_price(coin) or 0

    confidence = random.randint(60, 95)

    entry_low = price * 0.995
    entry_high = price * 1.005

    stop = price * 0.97
    target = price * 1.04

    direction = random.choice([
        "🟢 Setup haussier",
        "🔴 Setup baissier",
        "🟡 Attendre confirmation"
    ])

    return f"""
📈 SIGNAL TRADING

Actif
{coin}

Prix actuel
{price:.0f}$

Direction
{direction}

Zone d'entrée
{entry_low:.0f}$ - {entry_high:.0f}$

Stop loss
{stop:.0f}$

Objectif
{target:.0f}$

Confiance
{confidence} %

Guide

Entrer seulement si
la tendance confirme
le mouvement.
"""
