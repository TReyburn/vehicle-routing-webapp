from flask import render_template
from flask_restful import Resource


class HomePage(Resource):

    def __init__(self):
        self.home_page = 'index.html'

    def get(self):
        return render_template(self.home_page), 200
