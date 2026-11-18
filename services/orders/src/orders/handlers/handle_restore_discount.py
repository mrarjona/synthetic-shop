"""Handles the restore command for a discount."""
from orders.repository.memory import ORDERS


def handle(key: str, data: dict) -> dict:
    item = ORDERS.items.get(key)
    return {"discount": key, "found": item is not None, "action": "restore"}
