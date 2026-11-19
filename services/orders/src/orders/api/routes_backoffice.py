from orders.api.deps import customers_repo, orders_repo
from orders.domain.status import Status


def list_all() -> list[str]:
    return list(orders_repo().items)


def count_by_status() -> dict[str, int]:
    counts: dict[str, int] = {}
    for order in orders_repo().items.values():
        counts[order.status.value] = counts.get(order.status.value, 0) + 1
    return counts


def cancelled() -> list[str]:
    return [o.id for o in orders_repo().items.values() if o.status is Status.CANCELLED]


def customers() -> list[str]:
    return [c.email for c in customers_repo().items.values()]


ROUTES = {
    "GET /backoffice/orders": list_all,
    "GET /backoffice/orders/by-status": count_by_status,
    "GET /backoffice/orders/cancelled": cancelled,
    "GET /backoffice/customers": customers,
}
