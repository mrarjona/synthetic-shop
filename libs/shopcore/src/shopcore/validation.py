from shopcore.errors import ValidationError


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)
