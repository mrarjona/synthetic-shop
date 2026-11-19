from orders.config import DEFAULT_COUNTRY
from orders.domain.line_item import LineItem
from shopcore.money import ZERO, Money
from shopcore.tax import tax_for


def subtotal(items: list[LineItem]) -> Money:
    total = ZERO
    for item in items:
        total = total + item.total
    return total


def grand_total(items: list[LineItem], country: str = DEFAULT_COUNTRY) -> Money:
    base = subtotal(items)
    return base + tax_for(base, country)
