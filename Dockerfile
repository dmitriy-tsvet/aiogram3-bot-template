FROM python:3.10.1

WORKDIR /app

COPY . .

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt