#!/usr/bin/env python3

import fastapi
import uvicorn

from app.api import settleupapi

app = fastapi.FastAPI()


def configure():
    app.include_router(settleupapi.router)


configure()
if __name__ == '__main__':
    uvicorn.run(app)
