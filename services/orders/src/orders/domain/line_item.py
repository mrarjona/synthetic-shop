from dataclasses import dataclass
from decimal import Decimal

from shopcore.money import Money


@dataclass
class LineItem:
    sku: str
    quantity: int
    unit_price: Money

    @property
    def total(self) -> Money:
        return self.unit_price.times(self.quantity)


def item(sku: str, quantity: int, price: str) -> LineItem:
    return LineItem(sku, quantity, Money(Decimal(price)))
