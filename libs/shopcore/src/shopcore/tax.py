from decimal import Decimal

from shopcore.money import Money

RATES = {"ES": Decimal("0.21"), "PT": Decimal("0.23"), "FR": Decimal("0.20")}


def tax_for(amount: Money, country: str) -> Money:
    return Money((amount.amount * RATES.get(country, Decimal("0.21"))).quantize(Decimal("0.01")), amount.currency)
