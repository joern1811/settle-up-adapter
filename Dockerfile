FROM python:3.7-slim-buster

COPY requirements.txt .

RUN apt-get update && apt-get -y install gcc

RUN pip install -r requirements.txt

EXPOSE 80

COPY env_secrets_expand.sh .
COPY docker-entrypoint.sh .
COPY ./app /app

RUN chmod +x env_secrets_expand.sh
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["settle-up"]