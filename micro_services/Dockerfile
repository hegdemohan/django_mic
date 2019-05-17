FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt /requirement.txt
# RUN pip install -r /requirements.txt
RUN apk add --no-cache python3 postgresql-libs && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && python3 -m pip install -r requirement.txt --no-cache-dir && apk --purge del .build-deps

RUN mkdir /micro_services
WORKDIR /micro_services
COPY ./micro_services /micro_services