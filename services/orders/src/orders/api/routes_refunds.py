from orders.api.deps import orders_repo
from orders.services.refunds import approve, request_refund
from shopcore.money import Money


def post_refund(order_id: str, amount: str, reason: str) -> dict:
    refund = request_refund(orders_repo().get(order_id), Money(amount), reason)
    return {"refund": refund.id}


def post_approval(refund_id: str) -> dict:
    return {"refund": approve(refund_id).id, "approved": True}


ROUTES = {"POST /orders/{id}/refunds": post_refund, "POST /refunds/{id}/approval": post_approval}
