from dataclasses import dataclass
from decimal import Decimal

from shopcore.errors import ValidationError


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str = "EUR"

    def __add__(self, other: "Money") -> "Money":
        if other.currency != self.currency:
            raise ValidationError("currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def times(self, n: int) -> "Money":
        return Money(self.amount * n, self.currency)

    def percent_off(self, percent: int) -> "Money":
        if not 0 <= percent <= 100:
            raise ValidationError("a percentage between 0 and 100")
        return Money(self.amount * (Decimal(100 - percent) / 100), self.currency)


ZERO = Money(Decimal("0"))
