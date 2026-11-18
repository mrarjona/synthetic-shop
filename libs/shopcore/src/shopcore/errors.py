class ShopError(Exception):
    """Base error of the shop."""


class ValidationError(ShopError):
    pass


class NotFound(ShopError):
    pass
