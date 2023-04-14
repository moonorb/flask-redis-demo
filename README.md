
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






