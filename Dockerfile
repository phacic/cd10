FROM python:3.6-slim-stretch

# Set environment varibles

# Python won't try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensures our console output looks familiar and is not buffered by Docker
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# copy requirements
COPY ./requirements.txt /code/

VOLUME [ "/code" ]

# install requirements
RUN pip install -r requirements.txt

COPY . /code/

# # they don't seem to be install with the other requirements
RUN pip install django-redis==4.11.0 django-redis-cache==2.1.0 hiredis==1.0.1

# make script executable
RUN chmod u+x /code/collect_static.sh /code/migration.sh

# mount point for other files
RUN mkdir -p /config

VOLUME [ "/config" ]
