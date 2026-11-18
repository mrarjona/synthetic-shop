from orders.domain.line_item import LineItem
from shopcore.legacy_tax import legacy_tax
from shopcore.money import ZERO, Money


def subtotal(items: list[LineItem]) -> Money:
    total = ZERO
    for item in items:
        total = total + item.total
    return total


def grand_total(items: list[LineItem]) -> Money:
    base = subtotal(items)
    return base + legacy_tax(base)
