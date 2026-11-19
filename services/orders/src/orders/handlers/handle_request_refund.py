"""Handles the request command for a refund."""
from orders.repository.memory import ORDERS
from orders.services.refunds import PENDING


def handle(key: str, data: dict) -> dict:
    return {"refund": key, "pending": key in PENDING, "orders": len(ORDERS.items), "action": "request"}
