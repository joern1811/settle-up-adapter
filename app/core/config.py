from starlette.config import Config

config = Config(".env")

SETTLE_UP_API_KEY: str = config('SETTLE_UP_API_KEY')
SETTLE_UP_AUTH_DOMAIN: str = config('SETTLE_UP_AUTH_DOMAIN')
SETTLE_UP_DATABASE_URL: str = config('SETTLE_UP_DATABASE_URL')
SETTLE_UP_STORAGE_BUCKET: str = config('SETTLE_UP_STORAGE_BUCKET')

SETTLE_UP_USER: str = config('SETTLE_UP_USER')
SETTLE_UP_PASSWORD: str = config('SETTLE_UP_PASSWORD')
