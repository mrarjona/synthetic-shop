from decimal import Decimal

from orders.domain.status import Status
from orders.services.refunds import approve, request_refund
from shopcore.money import Money


def test_full_refund(order):
    refund = request_refund(order, order.total, "damaged")
    approve(refund.id)
    assert order.status is Status.REFUNDED


def test_partial_refund(order):
    approve(request_refund(order, Money(Decimal("1")), "late").id)
    assert order.status is not Status.REFUNDED
