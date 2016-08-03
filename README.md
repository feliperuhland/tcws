# tcws
TechCrunch WebService

The unique dependency for running this project is Docker and Docker Compose.

But first, you will need a config file ``.env``:

```
DATABASE_URL=postgres://postgres@db:5432/postgres
DJANGO_SETTINGS_MODULE=tcws.settings
RABBITMQ_URL=amqp://rabbitmq
SECRET_KEY=SOM3KEY
TASK_MINUTES=10
```

Then just call ``docker-compose up -d``.
