from orders.domain.order import Order
from orders.domain.refund import Refund
from orders.events.publisher import publish
from shopcore.money import Money

PENDING: dict[str, Refund] = {}


def request_refund(order: Order, amount: Money, reason: str) -> Refund:
    refund = Refund(order, amount, reason)
    PENDING[refund.id] = refund
    publish("refund.requested", {"refund": refund.id, "order": order.id})
    return refund


def approve(refund_id: str) -> Refund:
    refund = PENDING.pop(refund_id)
    refund.approved = True
    refund.order.mark_refunded(refund.amount)
    publish("refund.approved", {"refund": refund.id})
    return refund
