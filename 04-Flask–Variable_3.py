from flask import Flask

app = Flask(__name__)


@app.route('/flask') # Without / ; http://127.0.0.1/flask/ will error
def hello_flask():
    return 'Hello Flask'


@app.route('/python/') # With / at end
def hello_python():
    return 'Hello Python'


if __name__ == '__main__':
    app.run()
