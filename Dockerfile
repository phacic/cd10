FROM python:3.6-slim-stretch

# Set environment varibles
# ensures our console output looks familiar and is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1
# Python won't try to write .pyc files
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# copy requirements
COPY ./requirements.txt /code/

VOLUME [ "/code" ]

# install requirements
RUN pip install -r requirements.txt

COPY . /code/

# mount point for other files
RUN mkdir -p /config

VOLUME [ "/config" ]
