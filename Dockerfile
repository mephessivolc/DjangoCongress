FROM python:latest

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

#install dependences
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
