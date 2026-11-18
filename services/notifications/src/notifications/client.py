from notifications.dispatcher import dispatch
from shopcore.events import Event


class NotifyClient:
    """In-process client; a queue would sit here in production."""

    def notify(self, event: Event, email: str | None = None) -> list[str]:
        return dispatch(event, email=email)
