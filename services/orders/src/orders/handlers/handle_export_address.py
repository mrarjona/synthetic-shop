"""Handles the export command for a address."""
from orders.repository.memory import CUSTOMERS


def handle(key: str, data: dict) -> dict:
    item = CUSTOMERS.items.get(key)
    return {"address": key, "found": item is not None, "action": "export"}
