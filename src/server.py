from flask import Flask, request
HOST = "0.0.0.0"
PORT = 3000
DEBUG = False

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'alive server'


@app.route('/update', methods=['post'])
def update():
    data = request.get_json()
    print(data)
    return data


if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)
