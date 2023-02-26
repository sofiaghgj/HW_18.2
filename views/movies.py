from flask import request
from flask_restx import Resource, Namespace

from dao.models.movie import MovieSchema
from implements import movie_service

movie_ns = Namespace('movie')
@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        name = movie_service.get_all()
        return MovieSchema(many=True).dump(name)

    def post(self):
        name = movie_service.create(request.json)
        return MovieSchema().dump(name)


@movie_ns.route('/<int:mid>')
class GenreView(Resource):
    def get(self, mid):
        name = movie_service.get_one(mid)
        return MovieSchema().dump(name)

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204

    def update(self, mid):
        name = movie_service.update(mid, request.json)
        return MovieSchema().dump(name)