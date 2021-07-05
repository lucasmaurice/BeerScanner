## Development

### With docker and docker-compose

#### Make migration

```
docker-compose run web python manage.py makemigrations DrinkConsumption
```

#### Migrate

```
docker-compose run web python manage.py migrate
```
