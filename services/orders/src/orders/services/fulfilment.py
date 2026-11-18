from orders.domain.order import Order
from orders.domain.status import Status
from orders.events.publisher import publish


def ship(order: Order) -> None:
    order.status = Status.SHIPPED
    publish("order.shipped", {"order": order.id})
