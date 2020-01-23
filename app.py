from flask import Flask, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
