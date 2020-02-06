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

# make script executable
RUN chmod u+x /code/collect_static.sh /code/migration.sh /code/load_data.sh

# mount point for other files
RUN mkdir -p /config

VOLUME [ "/config" ]
