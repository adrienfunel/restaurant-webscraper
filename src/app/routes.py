from flask import requests
from flask_restplus import Resource, fields, regparse

from main import fetch_data

data_args = regparse.RequestParser()
data_args.add_argument('ratings', type=float, required=False)
data_args.add_argument('reviews', type=int, required=False)
data_args.add_argument('price', type=int, required=False)
data_args.add_argument('cuisine', type=str, required=False)
data_args.add_argument('location', type=str, required=False)


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
                ratings, reviews, price, cuisine, location = arg_parser(args)
                response = fetch_data(ratings, reviews, price, cuisine, location)
                return response
            except Exception:
                pass

def arg_parser(args):
    ratings = args['ratings'] if args['ratings'] else None
    reviews = args['reviews'] if args['reviews'] else None
    price = args['price'] if args['price'] else None
    cuisine = args['cuisine'] if args['cuisine'] else None
    location = args['location'] if args['location'] else None
    return ratings, reviews, price, cuisine, location
