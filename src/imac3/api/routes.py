"""
IMAC3 AI Route Discovery Module

Public API Information Layer
"""


AVAILABLE_ROUTES = [
    "/",
    "/api/status",
    "/system",
    "/agent",
    "/decision",
    "/automation",
    "/data",
    "/config"
]


def get_available_routes():

    return {
        "system": "IMAC3 AI",
        "available_routes": AVAILABLE_ROUTES,
        "message": "Available API endpoints"
    }
