"""Handles the cancel command for a customer."""
from orders.events.publisher import publish
from orders.repository.memory import CUSTOMERS


def handle(key: str, data: dict) -> dict:
    item = CUSTOMERS.items.get(key)
    publish("customer.canceld", {"id": key})
    return {"customer": key, "found": item is not None, "action": "cancel"}
