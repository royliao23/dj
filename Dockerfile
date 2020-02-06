FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /dj
WORKDIR /dj
COPY requirements.txt /dj/
RUN pip install -r requirements.txt
COPY . /dj/