from flask import Flask
import os
from redis import Redis
from prometheus_flask_exporter import PrometheusMetrics

redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'),
              port=os.getenv('REDIS_PORT', 6379))
app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    redis.incr('hits')
    hits = int(redis.get('hits'))
    return f"Hits: {hits}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
