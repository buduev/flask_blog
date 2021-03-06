# Простенький сервис блогов с использованием библиотеки Flask на базе [прототипа](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru)

В отличие от прототипа в качестве базы данных использован Postgres.

Для тестирования на локальной Windows машине был запущен [Docker Desktop для Windows с помощью WSL 2](https://docs.microsoft.com/ru-ru/windows/wsl/tutorials/wsl-containers)

Возможные варианты развертывания - Docker/Kubernetes

### Docker

Построить образ и запустить контейнер:
```sh
~/.docker/flask_blog/app$ docker-compose up -d --build
```
Для запуска в отладочном режиме
```sh
~/.docker/flask_blog/app$ docker-compose up
```

Приложение доступно по ссылке

[http://localhost:5001/](http://localhost:5001/)

### Kubernetes

Был использован кластер k8s предоставляемый Docker Desktop

Желающим использовать Kubernetes Dashboard - [сюда](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

А [здесь](https://andrewlock.net/running-kubernetes-and-the-dashboard-with-docker-desktop/) подробней и с метриами

Создать пространство имен flask:
```sh
~/.docker/flask_blog/app$ kubectl create namespace flask
```


https://testdriven.io/blog/running-flask-on-kubernetes/

https://www.8host.com/blog/bazovoe-razvertyvanie-prilozheniya-flask-s-pomoshhyu-kubernetes-i-docker/

https://medium.com/featurepreneur/deploying-a-flask-app-to-kubernetes-f05c93866aff
