# Flask-Redis Deployment

![Alt text](https://github.com/moonorb/flask-redis-demo/blob/main/images/flask-redis.PNG)

This is a super simple demo application to practice and experiment with K8s using a Python/Flask application.
It uses a redis backend and displays the page hits.

Deploying the app: 
```
git clone https://github.com/moonorb/flask-redis-demo.git
cd flask-redis-demo
kubectl create ns flask
kubectl create -f flask-redis-demo -n flask
```


Building the image
```
cd app
podman build -t docker.io/moonorb/flask-redis:v4 .
podman images
podman push docker.io/moonorb/flask-redis:v3
```


