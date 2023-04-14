# Flask-Redis Deployment

<<<<<<< HEAD
![Alt text](https://github.com/moonorb/images/blob/main/images/flask-redis.PNG )
=======
![Alt text](https://gitlab.com/moonorb/demo/-/raw/main/images/flask-redis.PNG )
>>>>>>> 444db010760cbe3f80baebf59f38dfcf66d0b4b0

This is a super simple demo application to practice and experiment with K8s using a Python/Flask application.
It uses a redis backend and displays the page hits.

Deploying the app: 
```
git clone https://gitlab.com/moonorb/flask-redis-demo.git
cd flask-redis-demo
kubectl create ns flask
kubectl create -f flask-redis-demo -n flask
```


Building the image
```
cd app
podman build -t docker.io/moonorb/flask-redis:v3
podman images
podman push docker.io/moonorb/flask-redis:v3
```






