from dataclasses import dataclass, field

from orders.domain.order import Order
from shopcore.clock import now
from shopcore.ids import new_id
from shopcore.money import Money
from shopcore.validation import require


@dataclass
class Refund:
    order: Order
    amount: Money
    reason: str
    id: str = field(default_factory=lambda: new_id("ref"))
    requested_at: str = field(default_factory=lambda: now().isoformat())
    approved: bool | None = None

    def __post_init__(self) -> None:
        require(self.amount.amount <= self.order.total.amount, "refund larger than the order")
