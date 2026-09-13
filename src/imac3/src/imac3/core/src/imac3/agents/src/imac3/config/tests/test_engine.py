from src.imac3.core.engine import IMAC3Engine


def test_engine():
    engine = IMAC3Engine()
    assert engine.name == "IMAC3 AI"
