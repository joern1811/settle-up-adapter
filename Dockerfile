FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 80

COPY env_secrets_expand.sh .
COPY run.sh .
COPY ./app /app

RUN chmod +x env_secrets_expand.sh
RUN chmod +x run.sh

ENTRYPOINT ["./run.sh"]