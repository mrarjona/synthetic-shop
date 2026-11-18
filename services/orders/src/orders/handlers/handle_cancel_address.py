"""Handles the cancel command for a address."""
from orders.events.publisher import publish
from orders.repository.memory import CUSTOMERS


def handle(key: str, data: dict) -> dict:
    item = CUSTOMERS.items.get(key)
    publish("address.canceld", {"id": key})
    return {"address": key, "found": item is not None, "action": "cancel"}
