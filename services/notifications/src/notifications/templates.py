TEMPLATES = {
    "refund.requested": "We received your refund request for order {order}.",
    "refund.approved": "Your refund {refund} was approved.",
    "order.shipped": "Your order {order} is on its way.",
}


def render(name: str, payload: dict) -> str:
    return TEMPLATES[name].format(**payload)
