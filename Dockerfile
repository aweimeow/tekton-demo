# syntax=docker/dockerfile:1
FROM python:3.9
COPY . /
CMD python /web.py

EXPOSE 8000
