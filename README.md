# Statetrace Django Demo

Works with [Statetrace](https://statetrace.com).

Run demo with docker-compose.
```bash
docker-compose up
```

In other terminal create the superuser to login:
```bash
docker-compose run web python manage.py createsuperuser
```

## Routes

* Login to Statetrace by accessing `http://localhost:9999`
* Create a new Poll by going to `http://localhost:8000/admin`
* Vote on a Poll by going to `http://localhost:8000`
