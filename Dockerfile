FROM python:3.11

WORKDIR /app

RUN pip3 install Balethon
RUN pip3 install Flask

COPY . .

CMD ["python3", "bot.py"]
CMD ["python3", "app.py"]