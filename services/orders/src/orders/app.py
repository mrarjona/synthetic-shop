from orders.api import routes_backoffice, routes_customers, routes_health, routes_orders, routes_refunds


def create_app() -> dict:
    routes = {}
    for module in (routes_orders, routes_customers, routes_backoffice, routes_health, routes_refunds):
        routes.update(module.ROUTES)
    return routes
