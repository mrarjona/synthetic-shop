from orders.app import create_app


def test_routes():
    assert "GET /health" in create_app()
