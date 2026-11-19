from notifications.settings import SMTP_HOST


def send_email(to: str, body: str) -> str:
    return f"smtp://{SMTP_HOST}/{to}: {body}"
