from orders.domain.discount import apply_discount
from orders.domain.order import Order
from shopcore.money import Money


def price(order: Order, discount: int = 0) -> Money:
    return apply_discount(order.total, discount)
