# Flask-Redis Deployment

![Alt text](https://gitlab.com/moonorb/demo/-/raw/main/images/flask-redis.PNG )

This is a super simple demo application to practice and experiment with K8s using a Python/Flask application.
It uses a redis backend and displays the page hits.

Deploying the app: 
```
git clone https://gitlab.com/moonorb/flask-redis-demo.git
cd flask-redis-demo
kubectl create ns flask
kubectl create -f flask-redis-demo -n flask
```

In case you want to build the image yourself
```
git clone https://gitlab.com/moonorb/flask-redis-demo.git
cd app
podman build -t docker.io/moonorb/flask-redis:v3
podman images
podman push docker.io/moonorb/flask-redis:v3
```





