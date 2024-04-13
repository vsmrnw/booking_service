FROM python:3.11.9
LABEL authors="vs"

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
