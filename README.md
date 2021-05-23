# Простенкий сервис блогов на Flask на базе [прототипа](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru)
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

Рабочая ссылка

1. [http://localhost:5001/](http://localhost:5001/)
2. [http://localhost:5001/probe](http://localhost:5001/probe)

### Kubernetes

#### Minikube

Install and run [Minikube](https://kubernetes.io/docs/setup/minikube/):
