FROM python:3.11-bullseye

RUN apt-get update && apt-get install -y sudo
  
ENV PIP_NO_CACHE_DIR=off
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN mkdir /workspace
WORKDIR /workspace
