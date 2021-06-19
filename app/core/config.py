from starlette.config import Config

config = Config(".env")

SETTLE_UP_FIREBASE_API_KEY: str = config("SETTLE_UP_FIREBASE_API_KEY")
SETTLE_UP_FIREBASE_PROJECT_NAME: str = config("SETTLE_UP_FIREBASE_PROJECT_NAME")

SETTLE_UP_USER: str = config("SETTLE_UP_USER")
SETTLE_UP_PASSWORD: str = config("SETTLE_UP_PASSWORD")
