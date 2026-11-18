from decimal import Decimal

import pytest

from orders.domain.address import Address
from orders.domain.customer import Customer
from orders.domain.line_item import LineItem
from orders.domain.order import Order
from shopcore.money import Money


@pytest.fixture
def order():
    customer = Customer("Ada", "ada@example.com", Address("Calle 1", "Sevilla", "ES"))
    return Order(customer, [LineItem("sku-1", 2, Money(Decimal("10")))])
