# **Get Started**
Install

    git clone https://github.com/phacic/cd10.git

# **Run**

Docker is required to run the following commands.

    $ docker network create --gateway 172.16.2.1 --subnet 172.16.2.0/24 challenge-bridge

to create network on docker for the containers to run on

## First Run

**1 - run the server on docker**
    $ docker-compose up

wait for all the builds to complete then terminate with `CTRL+C. then

    $ docker-compose up -d

**2 - migrate models into database**

    $ docker-compose exec cd10 /code/migration.sh

on permission error (starting container process caused... permission error)

    $ docker-compose exec -u root cd10 sh -c "python manage.py makemigrations"
    $ docker-compose exec -u root cd10 sh -c "python manage.py migrate"

**3 - collect static files**

    $ docker-compose exec cd10 /code/collect_static.sh

on permission error (starting container process caused... permission error)
    
    $ docker-compose exec -u root cd10 sh -c "python manage.py collectstatic"

**4 - load initial data**

    $ docker-compose exec cd10 /code/load_data.sh

on permission error (starting container process caused... permission error)

    $ docker-compose exec -u root cd10 sh -c "python manage.py loaddata init-data.json"

## Subsequent runs
    $ docker-compose up -d

## On Windows

Enable shared volumes under Docker settings and in the `docker-compose-win.yml`replace the volumes drive letter with the drive you shared. E.g. if you shared c:

     volumes:
      - e:/data/redis/r1:/data

     volumes:
      - c:/data/redis/r1:/data

then for postgreSQL to work run the following to create the required volumne

    # docker volume create --name=postgres_data

So when running the commands under run you do this to specify the file

    $ docker-compose -f docker-compose-win.yml up -d




# **Endpoints**
## CD10 Category

- GET, POST `/cd10/categories/`

example data for to create a new one
    
    {
        "code": "A00",
        "title": "Cholera"
    }
    

- PUT, PATCH, DELETE `/cd10/categories/{id}`


## CD10 Diagnosis

- GET, POST `/cd10/diagnosis/`

example data for to create a new one
    
    {
        "category": 1,
        "code": 0,
        "full_code": "A000",
        "abbreviated_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
        "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
        "backward_compatible": true,
    }
    
- PUT, PATCH, DELETE `/cd10/diagnosis/{id}`

data structure returned

    {
        "id": 1,
        "category": 1,
        "code": 0,
        "full_code": "A000",
        "abbreviated_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
        "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
        "backward_compatible": true,
        "created": "2020-02-04T11:51:17.847000Z",
        "updated": "2020-02-04T11:51:17.847000Z",
        "category_detail": {
            "id": 1,
            "code": "A00",
            "title": "Cholera"
        }
    }

# ARCHITECTURAL CONSIDERATION

## caching
Cache is applied to reduce the request time for resources where applicable. Since the data does not change often it is advisable to cache the data so we don't hit the database on each request.


# DEVELOPMENT

Redis server has to be accessible to get cache working in development.

## *TODO*
Extend caching to diagnosis list. Page has to be cached on first request and cached data return on subsequent request. Page cache will have to be invalidated on create, update and delete of diagnosis.