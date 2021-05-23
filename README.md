# Простенкий сервис блогов на Flask на базе статьи
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru
# Изменение - в качестве базы данных использован Postgres
# Возможные варианты развертывания - Docker/Kubernetes

### Docker

Построить образ и запусить контейнер:
```sh
$ docker-compose up -d --build
```
Для запуска в отладочном режиме
```sh
$ docker-compose up
```


Run the migrations and seed the database:

```sh
$ docker-compose exec server python manage.py recreate_db
$ docker-compose exec server python manage.py seed_db
```

Test it out at:

1. [http://localhost:8080/](http://localhost:8080/)
1. [http://localhost:5001/books/ping](http://localhost:5001/books/ping)
1. [http://localhost:5001/books](http://localhost:5001/books)

### Kubernetes

#### Minikube

Install and run [Minikube](https://kubernetes.io/docs/setup/minikube/):
