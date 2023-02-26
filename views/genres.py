from flask import request
from flask_restx import Resource, Namespace

from dao.models.genre import GenreSchema
from implements import genre_service

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        name = genre_service.get_all()
        return GenreSchema(many=True).dump(name)

    def post(self):
        name = genre_service.create(request.json)
        return GenreSchema().dump(name)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        name = genre_service.get_one(gid)
        return GenreSchema().dump(name)

    def delete(self, gid):
        genre_service.delete(gid)
        return '', 204

    def update(self, gid):
        name = genre_service.update(gid, request.json)
        return GenreSchema().dump(name)