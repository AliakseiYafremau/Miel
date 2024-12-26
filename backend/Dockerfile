FROM python:3.12-slim

WORKDIR /backend

COPY ./.env .env
COPY ./requirements.txt /backend/requirements.txt
COPY ./alembic.ini /backend/alembic.ini
COPY ./migrations /backend/migrations

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /backend/requirements.txt

COPY ./app/ /backend/app/

COPY ./static /backend/static
COPY ./templates /backend/templates

CMD bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; alembic upgrade head && uvicorn app.main:app --host 0.0.0.0'