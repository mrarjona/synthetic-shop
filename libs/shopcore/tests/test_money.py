from decimal import Decimal

from shopcore.money import Money


def test_add():
    assert Money(Decimal("1")) + Money(Decimal("2")) == Money(Decimal("3"))
