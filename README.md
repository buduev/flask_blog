# Простенький сервис блогов с использованием библиотеки Flask на базе [прототипа](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru) с примерами деплоя в Docker и Kubernetes

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
Будем использовать образы созданные на предыдущем шаге

Я не ставил отдельно minikube, был использован кластер k8s предоставляемый Docker Desktop

Для мониторинга создаваемых объектов можно использовать плагин VS, но мне удобнее [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

А [здесь](https://andrewlock.net/running-kubernetes-and-the-dashboard-with-docker-desktop/) подробней и с метриками

Создадим собственное пространство имен:
```sh
~/.docker/flask_blog/app$ kubectl create namespace igrich
```

Создать секреты для базы данных. Секреты хранятся в base64x, поэтому сначала закодируем креды:

```sh
$ echo -n "username" | base64
$ echo -n "password" | base64
```


```sh
~/.docker/flask_blog/app$ kubectl apply -f ./k8s/secret.yml -n igrich
```

Создаем хранилище с помощью [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) и [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) для хранения данных Postgres вне Pod.

```sh
~/.docker/flask_blog/app$ kubectl apply -f ./k8s/postgres-storage.yml -n igrich
~/.docker/flask_blog/app$ kubectl apply -f ./k8s/postgres-service.yml -n igrich
```

Создаем сервис блога
```sh
~/.docker/flask_blog/app$ kubectl apply -f ./k8s/flask-service.yml -n igrich
```


```sh
$ kubectl port-forward deployment/flask-deployment -n igrich 5001:5001
```
 

https://testdriven.io/blog/running-flask-on-kubernetes/

https://www.8host.com/blog/bazovoe-razvertyvanie-prilozheniya-flask-s-pomoshhyu-kubernetes-i-docker/

https://medium.com/featurepreneur/deploying-a-flask-app-to-kubernetes-f05c93866aff
