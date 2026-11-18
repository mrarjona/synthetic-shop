from orders.api.deps import orders_repo
from orders.api.schemas import order_json
from orders.services.checkout import checkout


def get_order(order_id: str) -> dict:
    return order_json(orders_repo().get(order_id))


ROUTES = {"GET /orders/{id}": get_order, "POST /checkout": checkout}
