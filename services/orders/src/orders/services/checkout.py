from orders.domain.order import Order
from orders.events.publisher import publish
from orders.repository.memory import ORDERS
from orders.services.inventory import reserve
from orders.services.pricing import price


def checkout(order: Order) -> dict:
    for item in order.items:
        if not reserve(item.sku, item.quantity):
            return {"ok": False, "sku": item.sku}
    ORDERS.put(order.id, order)
    publish("order.created", {"order": order.id, "total": str(price(order).amount)})
    return {"ok": True, "order": order.id}
