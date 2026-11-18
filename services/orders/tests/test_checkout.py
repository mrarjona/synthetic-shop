from orders.services import inventory
from orders.services.checkout import checkout


def test_checkout(order):
    inventory.STOCK["sku-1"] = 5
    assert checkout(order)["ok"]
