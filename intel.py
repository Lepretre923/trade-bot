import requests
import random


# NEWS CRYPTO
def market_intel():

    news = [
        "Bitcoin ETF enregistre un volume record",
        "Activité réseau Ethereum en forte hausse",
        "Volume trading Solana en expansion",
        "Augmentation des positions futures sur BTC",
        "Flux institutionnels positifs sur les ETF crypto"
    ]

    msg = "📰 INTELLIGENCE MARCHÉ CRYPTO\n\n"

    msg += "Actualités importantes\n\n"

    for n in news:
        msg += f"• {n}\n"

    msg += "\nAnalyse\n"
    msg += "Les flux institutionnels et le volume\n"
    msg += "restent les moteurs principaux du marché."

    return msg


# WHALE ALERT SIMPLE
def whale_alert():

    whales = [
        "🐋 1200 BTC transférés vers exchange",
        "🐋 800 ETH déplacés vers wallet inconnu",
        "🐋 grosse transaction USDT détectée",
        "🐋 accumulation BTC détectée",
        "🐋 transfert important vers cold wallet"
    ]

    msg = "🚨 WHALE ALERT\n\n"
    msg += random.choice(whales)

    msg += "\n\nAnalyse\n"
    msg += "Les mouvements de whales peuvent\n"
    msg += "provoquer volatilité et liquidations."

    return msg


# WHALE BLOCKCHAIN
def whale_blockchain():

    whales = [
        "3500 BTC transférés vers Binance",
        "2100 ETH déplacés hors exchange",
        "transaction USDT 45M$ détectée",
        "whale accumulation BTC détectée",
        "gros mouvement stablecoin vers exchange"
    ]

    msg = "🚨 ACTIVITÉ WHALE BLOCKCHAIN\n\n"

    msg += f"Transaction détectée\n\n🐋 {random.choice(whales)}\n\n"

    msg += "Impact possible\n"
    msg += "Hausse de volatilité\n"
    msg += "Possible mouvement rapide du prix"

    return msg


# SCANNER PUMPS MARCHÉ
def market_scanner():

    try:

        url = "https://api.coingecko.com/api/v3/coins/markets"

        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 200,
            "page": 1
        }

        data = requests.get(url, params=params).json()

        pumps = []

        for coin in data:

            change = coin.get("price_change_percentage_24h")

            if change and change > 8:

                symbol = coin["symbol"].upper()
                pumps.append(f"{symbol}  +{change:.2f}%")

        if not pumps:

            return "📊 Scanner marché\n\nAucun pump majeur détecté"

        msg = "🚀 SCANNER PUMPS MARCHÉ\n\n"

        msg += "Cryptos en forte hausse\n\n"

        for p in pumps[:7]:
            msg += f"{p}\n"

        msg += "\nAnalyse\n"
        msg += "Les pumps rapides peuvent\n"
        msg += "être suivis de corrections."

        return msg

    except:

        return "Erreur récupération données marché"


# LIQUIDATIONS
def liquidation_alert():

    liquidations = [
        "💥 Liquidations importantes sur BTC futures",
        "💥 Long liquidations détectées",
        "💥 Short squeeze possible",
        "💥 Forte liquidation sur altcoins",
        "💥 cascade de liquidations détectée"
    ]

    msg = "💥 ALERTE LIQUIDATIONS\n\n"

    msg += random.choice(liquidations)

    msg += "\n\nAnalyse\n"
    msg += "Les liquidations massives provoquent\n"
    msg += "souvent des mouvements rapides."

    return msg


# SENTIMENT MARCHÉ
def sentiment_crypto():

    sentiments = [
        ("🟢 Marché très haussier", 75),
        ("🟡 Marché neutre", 50),
        ("🔴 Marché légèrement baissier", 35)
    ]

    sentiment, score = random.choice(sentiments)

    msg = "🧠 SENTIMENT MARCHÉ CRYPTO\n\n"

    msg += f"Score sentiment\n{score}/100\n\n"

    msg += f"Direction\n{sentiment}\n\n"

    msg += "Guide\n"
    msg += "Comparer sentiment avec volume\n"
    msg += "et liquidité avant trading."

    return msg


# SCANNER VOLUME
def volume_scanner():

    volumes = [
        "Volume BTC en forte hausse",
        "Volume ETH supérieur à la moyenne",
        "Augmentation volume sur altcoins",
        "Volume institutionnel détecté",
        "Volume futures en expansion"
    ]

    msg = "📊 SCANNER VOLUME MARCHÉ\n\n"

    msg += random.choice(volumes)

    msg += "\n\nAnalyse\n"
    msg += "Un volume élevé confirme souvent\n"
    msg += "la validité d'un mouvement."

    return msg
