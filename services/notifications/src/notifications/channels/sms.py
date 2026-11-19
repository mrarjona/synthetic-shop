from notifications.settings import SMS_SENDER


def send_sms(to: str, body: str) -> str:
    return f"sms:{SMS_SENDER}->{to}: {body}"
