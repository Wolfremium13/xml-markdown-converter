FROM python:3.10

WORKDIR /app

COPY ./ ./

RUN pip install pipenv && \
  apt-get update && \
  apt-get install make

RUN make setup