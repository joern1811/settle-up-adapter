#!/bin/bash

source ./env_secrets_expand.sh

if [ "$1" = 'settle-up' ]; then
      exec uvicorn app.main:app --host 0.0.0.0 --port 80
fi

exec "$@"