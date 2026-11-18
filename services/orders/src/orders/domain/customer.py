from dataclasses import dataclass, field

from orders.domain.address import Address
from shopcore.ids import new_id


@dataclass
class Customer:
    name: str
    email: str
    address: Address
    id: str = field(default_factory=lambda: new_id("cus"))
