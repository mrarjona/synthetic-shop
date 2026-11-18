STOCK: dict[str, int] = {}


def reserve(sku: str, quantity: int) -> bool:
    if STOCK.get(sku, 0) < quantity:
        return False
    STOCK[sku] -= quantity
    return True
