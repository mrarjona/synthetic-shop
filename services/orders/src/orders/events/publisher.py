from shopcore.events import Event
from shopcore.logging import get_logger

log = get_logger("orders.events")


def publish(name: str, payload: dict) -> Event:
    event = Event(name, payload)
    log.info("event %s %s", event.name, event.id)
    return event
