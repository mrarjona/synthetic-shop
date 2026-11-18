from notifications.channels.email import send_email
from notifications.channels.sms import send_sms
from notifications.templates import TEMPLATES, render
from shopcore.events import Event
from shopcore.logging import get_logger

log = get_logger("notifications")


def dispatch(event: Event, email: str | None = None, phone: str | None = None) -> list[str]:
    if event.name not in TEMPLATES:
        return []
    body = render(event.name, event.payload)
    sent = [send_email(email, body)] if email else []
    sent += [send_sms(phone, body)] if phone else []
    log.info("sent %d notifications for %s", len(sent), event.name)
    return sent
