# Flask-Redis Helm Chart

![Alt text](https://gitlab.com/moonorb/demo/-/raw/main/images/chart_diagram.PNG )

- **flask-chart - Parent chart**
- **redis-chart - Subchart(child)**

This code uses a local chartmuseum.
Repository must me modified in flask-chart/Chart.yaml to use this code elsewhere.

### Install Helm
```
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh
```

Modify the values.yaml files if you need to. 
Check what will be deployed before running installation
```
helm template flask-chart
```

Deploy and check the charts
```
kubectl create ns flask
helm install my-flask flask-chart -n flask
helm list
```

Uninstall
```
helm uninstall my-flask -n flask
```





