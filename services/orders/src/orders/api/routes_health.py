def health() -> dict:
    return {"ok": True}


ROUTES = {"GET /health": health}
