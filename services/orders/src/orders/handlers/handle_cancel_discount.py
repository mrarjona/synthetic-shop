"""Handles the cancel command for a discount."""
from orders.events.publisher import publish
from orders.repository.memory import ORDERS


def handle(key: str, data: dict) -> dict:
    item = ORDERS.items.get(key)
    publish("discount.canceld", {"id": key})
    return {"discount": key, "found": item is not None, "action": "cancel"}
