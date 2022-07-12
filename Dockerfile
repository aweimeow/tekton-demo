# syntax=docker/dockerfile:1
FROM python:3.9
COPY . /app
CMD python /app/web.py

EXPOSE 8000
