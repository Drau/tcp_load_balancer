FROM python:3.10.2-slim

WORKDIR /server

CMD python tcp_server.py