FROM python:3.11

WORKDIR /app

RUN pip3 install Balethon
RUN pip3 install Flask
RUN pip3 install jwt

COPY . .

CMD ["python3", "bot.py"]