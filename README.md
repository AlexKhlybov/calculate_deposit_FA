# Simple application for calculating the deposit

## Get start:

STEP-1
```
docker-compose build
```

STEP-2
```
docker-compose up -d
```

STEP-3
```
http://0.0.0.0:8000/docs
```

For RUN tests
```
docker-compose run web pytest
```

For RUN test coverage
```
docker-compose run web pytest --cov=app app/tests/
```
