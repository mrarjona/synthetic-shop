from orders.domain.order import Order
from orders.repository.base import Repository


class OrdersRepository(Repository[Order]):
    def by_customer(self, customer_id: str) -> list[Order]:
        return [o for o in self.items.values() if o.customer.id == customer_id]
