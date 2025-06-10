from flask import Flask, Response
from prometheus_client import Counter, generate_latest




REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
app = Flask(__name__)

@app.route('/')
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return "Hello, World!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
