import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "EduGenie")

    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY",
        ""
    ).strip()

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )


settings = Settings()