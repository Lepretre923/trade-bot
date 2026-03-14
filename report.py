from market import get_price, top_crypto
from analysis import analyse
from signals import get_signal
from intel import market_intel, market_scanner, sentiment_crypto


def market_report():

    msg = "📊 RAPPORT COMPLET MARCHÉ\n"
    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # PRIX PRINCIPAUX
    msg += "💰 PRIX MARCHÉ\n\n"

    msg += get_price("BTC") + "\n"
    msg += get_price("ETH") + "\n\n"

    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # ANALYSE BTC
    msg += "📊 ANALYSE BTC\n\n"

    msg += analyse("BTC") + "\n\n"

    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # SIGNAL TRADING
    msg += "📈 SIGNAL TRADING\n\n"

    msg += get_signal() + "\n\n"

    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # INTEL MARCHÉ
    msg += "🧠 INTELLIGENCE MARCHÉ\n\n"

    msg += market_intel() + "\n\n"

    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # SCANNER
    msg += "🔎 SCANNER MARCHÉ\n\n"

    msg += market_scanner() + "\n\n"

    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # SENTIMENT
    msg += "📊 SENTIMENT MARCHÉ\n\n"

    msg += sentiment_crypto() + "\n\n"

    msg += "━━━━━━━━━━━━━━━━━━\n\n"

    # TOP CRYPTOS
    msg += "🚀 TOP CRYPTOS\n\n"

    msg += top_crypto()

    return msg
