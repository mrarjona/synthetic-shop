from orders.domain.status import Status


def test_cancel(order):
    order.cancel()
    assert order.status is Status.CANCELLED
