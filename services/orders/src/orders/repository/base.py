from typing import Generic, TypeVar

from shopcore.errors import NotFound

T = TypeVar("T")


class Repository(Generic[T]):
    def __init__(self) -> None:
        self.items: dict[str, T] = {}

    def get(self, key: str) -> T:
        if key not in self.items:
            raise NotFound(key)
        return self.items[key]

    def put(self, key: str, item: T) -> None:
        self.items[key] = item
