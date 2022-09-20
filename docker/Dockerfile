FROM python:3.8.5-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc cron \
  && apt-get clean

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --dev --system --deploy

COPY . .
EXPOSE 80
