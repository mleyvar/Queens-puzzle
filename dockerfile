# Python 3.6.7
FROM python:3.6.7-alpine3.6
# author of file
LABEL maintainer="Marco Polo Leyva <mleyvar@hotmail.com>"

RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq

EXPOSE 5433

RUN pip3 install psycopg2

RUN pip3 install sqlalchemy

WORKDIR /app

COPY . /app

ENV NUM_QUEENS 8

#ENTRYPOINT [“python”]

#CMD [“/app/source/main.py”]

