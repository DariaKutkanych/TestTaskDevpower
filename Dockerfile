FROM python:3.10

WORKDIR /myapp

COPY ./requirements.txt /myapp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /myapp/requirements.txt

COPY . /myapp


ENV app_host 0.0.0.0
ENV app_port 8000
