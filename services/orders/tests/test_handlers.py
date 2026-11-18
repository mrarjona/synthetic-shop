from orders.handlers.handle_create_order import handle


def test_create_unknown():
    assert handle("nope", {})["found"] is False
