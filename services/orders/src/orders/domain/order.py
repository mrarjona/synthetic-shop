from dataclasses import dataclass, field

from orders.domain.customer import Customer
from orders.domain.line_item import LineItem
from orders.domain.status import Status
from orders.domain.totals import grand_total
from shopcore.ids import new_id
from shopcore.money import Money


@dataclass
class Order:
    customer: Customer
    items: list[LineItem]
    status: Status = Status.NEW
    id: str = field(default_factory=lambda: new_id("ord"))
    refunded: Money | None = None

    @property
    def total(self) -> Money:
        return grand_total(self.items)

    def cancel(self) -> None:
        self.status = Status.CANCELLED

    def mark_refunded(self, amount: Money) -> None:
        self.refunded = amount if self.refunded is None else self.refunded + amount
        if self.refunded.amount >= self.total.amount:
            self.status = Status.REFUNDED
