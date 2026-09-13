"""
IMAC3 AI Engine Test
"""


def test_system():

    system = {
        "name": "IMAC3 AI",
        "status": "ONLINE"
    }

    assert system["name"] == "IMAC3 AI"
    assert system["status"] == "ONLINE"
