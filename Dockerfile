FROM python:3.10

RUN pip install aiohttp

COPY . /app

WORKDIR /app

CMD ["python", "main.py"]