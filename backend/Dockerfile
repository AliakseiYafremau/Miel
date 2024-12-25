FROM python:3.12-slim

WORKDIR /app

COPY ./.env .env
COPY ./requirements.txt /app/requirements.txt
COPY ./alembic.ini /app/alembic.ini
COPY ./migrations /app/migrations

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app/ /app/app/