from orders.services.pricing import price


def test_discount(order):
    assert price(order, 50).amount < order.total.amount
