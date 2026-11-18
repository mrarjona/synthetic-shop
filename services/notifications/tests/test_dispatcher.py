from notifications.dispatcher import dispatch
from shopcore.events import Event


def test_unknown_event_sends_nothing():
    assert dispatch(Event("nope", {})) == []
