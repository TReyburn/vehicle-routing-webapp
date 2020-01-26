from flask import Flask, render_template
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
