"""Handles the restore command for a customer."""
from orders.repository.memory import CUSTOMERS


def handle(key: str, data: dict) -> dict:
    item = CUSTOMERS.items.get(key)
    return {"customer": key, "found": item is not None, "action": "restore"}
