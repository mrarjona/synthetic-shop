"""Tax rules of the first checkout. Kept until the orders service moves to shopcore.tax."""
from decimal import Decimal

from shopcore.money import Money


def legacy_tax(amount: Money) -> Money:
    return Money(amount.amount * Decimal("0.18"), amount.currency)
