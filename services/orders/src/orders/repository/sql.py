from orders.config import DATABASE_URL
from orders.domain.order import Order


def save(order: Order) -> str:
    return f"INSERT INTO orders VALUES ('{order.id}') -- {DATABASE_URL}"
