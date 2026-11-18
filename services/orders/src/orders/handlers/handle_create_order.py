"""Handles the create command for a order."""
from orders.events.publisher import publish
from orders.repository.memory import ORDERS


def handle(key: str, data: dict) -> dict:
    item = ORDERS.items.get(key)
    publish("order.created", {"id": key})
    return {"order": key, "found": item is not None, "action": "create"}
