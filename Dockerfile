FROM python:3.11

WORKDIR /app

RUN pip3 install Balethon

COPY . .

CMD ["python3", "main.py"]