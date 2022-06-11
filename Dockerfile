FROM python:3.7-alpine as build

RUN apk upgrade --no-cache
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo

WORKDIR /source

RUN python3 -m venv /source/.venv

COPY requirements.txt /source

RUN . /source/.venv/bin/activate && \
  python3 -m ensurepip --upgrade && \
  python3 -m pip install -r /source/requirements.txt

FROM python:3.7-alpine as final

RUN apk upgrade --no-cache

WORKDIR /source

COPY --from=build /source /source
RUN . /source/.venv/bin/activate

EXPOSE 80

COPY env_secrets_expand.sh .
COPY docker-entrypoint.sh .
COPY ./app ./app

RUN chmod +x env_secrets_expand.sh
RUN chmod +x docker-entrypoint.sh

HEALTHCHECK --interval=5s --timeout=10s CMD nc -vz localhost 80 || exit 1
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["settle-up"]
