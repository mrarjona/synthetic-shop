"""Handles the archive command for a order."""
from orders.repository.memory import ORDERS


def handle(key: str, data: dict) -> dict:
    item = ORDERS.items.get(key)
    return {"order": key, "found": item is not None, "action": "archive"}
