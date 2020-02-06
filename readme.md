# **Get Started**
Install

    git clone https://github.com/phacic/cd10.git

# **Run**

Docker is required to run the following commands.

## First Run

**1 - run the server on docker**

    $ docker-compose up -d

**2 - migrate models into database**

    $ docker-compose exec cd10 /code/migration.sh

**3 - collect static files**

    $ docker-compose exec cd10 /code/collect_static.sh

**4 - load initial data**

    $ docker-compose exec cd10 /code/load_data.sh

## Subsequent runs
    $ docker-compose up -d


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