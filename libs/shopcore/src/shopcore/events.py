from dataclasses import dataclass, field
from typing import Any

from shopcore.clock import now
from shopcore.ids import new_id


@dataclass
class Event:
    name: str
    payload: dict[str, Any]
    id: str = field(default_factory=lambda: new_id("evt"))
    at: str = field(default_factory=lambda: now().isoformat())
