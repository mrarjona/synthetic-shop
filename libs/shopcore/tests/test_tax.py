from decimal import Decimal

from shopcore.money import Money
from shopcore.tax import tax_for


def test_spain():
    assert tax_for(Money(Decimal("100")), "ES").amount == Decimal("21.00")
