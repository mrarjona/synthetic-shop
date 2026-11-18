from orders.domain.order import Order


def order_json(order: Order) -> dict:
    return {"id": order.id, "status": order.status.value, "total": str(order.total.amount)}
