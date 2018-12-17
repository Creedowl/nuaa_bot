FROM python:3.7-alpine
MAINTAINER creedowl
WORKDIR /bot/
COPY nuaa_bot nuaa_bot
COPY requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev --no-cache
RUN pip install -r requirements.txt
EXPOSE 8000
CMD "gunicorn -w 2 -b 0.0.0.0:8000 nuaa_bot:app"