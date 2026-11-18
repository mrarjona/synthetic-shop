from decimal import Decimal

from shopcore.money import Money


def apply_discount(amount: Money, percent: int) -> Money:
    return Money(amount.amount * (Decimal(100 - percent) / 100), amount.currency)
