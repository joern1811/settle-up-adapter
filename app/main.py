#!/usr/bin/env python3

import fastapi
import uvicorn

from app.api import settleupapi

app = fastapi.FastAPI(
    title="Settle-Up-REST-API",
    description="REST-API-Adapter to the settle-up firebase database",
    version="0.0.1"
)


def configure():
    app.include_router(settleupapi.router)


configure()
if __name__ == '__main__':
    uvicorn.run(app)
