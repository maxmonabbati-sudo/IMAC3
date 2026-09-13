from src.imac3.core.engine import IMAC3Engine


def test_engine():
    engine = IMAC3Engine()

    status = engine.status()

    assert status["system"] == "IMAC3 AI"
    assert status["state"] == "online"
