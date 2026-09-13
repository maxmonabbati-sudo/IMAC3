"""
IMAC3 AI Platform Launcher
"""

import uvicorn


if __name__ == "__main__":

    uvicorn.run(
        "src.imac3.api.fastapi_service:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
