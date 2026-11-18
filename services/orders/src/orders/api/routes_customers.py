from orders.api.deps import customers_repo


def get_customer(customer_id: str) -> dict:
    c = customers_repo().get(customer_id)
    return {"id": c.id, "name": c.name}


ROUTES = {"GET /customers/{id}": get_customer}
