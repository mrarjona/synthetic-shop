from notifications.client import NotifyClient
from shopcore.events import Event
from shopcore.logging import get_logger

log = get_logger("orders.events")
notifier = NotifyClient()


def publish(name: str, payload: dict, email: str | None = None) -> Event:
    event = Event(name, payload)
    log.info("event %s %s", event.name, event.id)
    notifier.notify(event, email=email)
    return event
