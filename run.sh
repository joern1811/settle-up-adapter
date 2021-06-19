#!/bin/sh

. ./env_secrets_expand.sh

uvicorn app.main:app --host 0.0.0.0 --port 80