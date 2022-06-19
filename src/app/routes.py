from flask import requests
from flask_restplus import Resource, fields, regparse

from main import fetch_data

data_args = regparse.RequestParser()
data_args.add_argument('cuisine', type=str, required=False)

def setup_routes(app):
    name_space = app.namespace('AltDataScraper', description='Scrap alternative data from a website')

    @name_space.route('/')
    class GetRestaurantInfo(Resource):
        @app.doc({200:'OK',
            400:'Invalid argument',
            500:'Internal service error'}
        )
        @app.expect(data_args)
        def get(self):
            try:
                args = data_args.parse_args()
                cuis_type = args['cuisine']
                response = fetch_data(cuis_type)
                return response
