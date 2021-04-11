"""Role testing files using testinfra."""


def test_webhook2telegram_bin(host):
    """Validate /usr/bin/ file."""
    f = host.file("/usr/bin/webhook2telegram")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_webhook2telegram_running_and_enabled(host):
    webhook = host.service("webhook2telegram")
    assert webhook.is_running
    assert webhook.is_enabled

