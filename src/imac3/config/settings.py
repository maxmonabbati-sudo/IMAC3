"""
IMAC3 AI Configuration Layer
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):

        self.app_name = os.getenv(
            "APP_NAME",
            "IMAC3 AI"
        )

        self.version = os.getenv(
            "VERSION",
            "0.1.0"
        )

        self.environment = os.getenv(
            "ENVIRONMENT",
            "development"
        )

        self.api_status = "ONLINE"


    def info(self):

        return {
            "name": self.app_name,
            "version": self.version,
            "environment": self.environment,
            "status": self.api_status
        }


settings = Settings()
