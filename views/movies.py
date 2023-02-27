from flask import request
from flask_restx import Resource, Namespace

from dao.models.movie import MovieSchema
from implements import movie_service

movie_ns = Namespace('movie')
@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        filters = {}
        if director_id := request.args.get('director_id'):
            filters['director_id'] = director_id
        if genre_id := request.args.get('genre_id'):
            filters['genre_id'] = genre_id
        if year := request.args.get('year'):
            filters['year'] = year
        name = movie_service.get_all(filters=filters)
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