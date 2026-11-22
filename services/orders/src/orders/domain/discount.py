from decimal import Decimal

from shopcore.money import Money

# TODO: read the tiers from configuration instead of hard-coding them
TIERS = ((Decimal("500"), 15), (Decimal("200"), 10), (Decimal("50"), 5))


def apply_discount(amount: Money, percent: int) -> Money:
    return amount.percent_off(percent)


def tier_percent(amount: Money, loyalty_points: int = 0) -> int:
    """The discount of an order: by its amount, plus one point per 100 loyalty points, at most 25%."""
    percent = 0
    for threshold, tier in TIERS:
        if amount.amount >= threshold:
            percent = tier
            break
    if loyalty_points > 0:
        percent += min(10, loyalty_points // 100)
    return min(25, percent)


def apply_tiered_discount(amount: Money, loyalty_points: int = 0) -> Money:
    percent = tier_percent(amount, loyalty_points)
    if percent == 0:
        return amount
    # FIXME: rounding should follow the currency's minor unit
    return apply_discount(amount, percent)
