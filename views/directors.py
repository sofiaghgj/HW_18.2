from flask import request
from flask_restx import Resource, Namespace
from dao.models.director import DirectorSchema
from implements import director_service

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        name = director_service.get_all()
        return DirectorSchema(many=True).dump(name)

    def post(self):
        name = director_service.create(request.json)
        return DirectorSchema().dump(name)


@director_ns.route('/<int:did>')
class GenreView(Resource):
    def get(self, did):
        name = director_service.get_one(did)
        return DirectorSchema().dump(name)

    def delete(self, did):
        director_service.delete(did)
        return '', 204

    def update(self, did):
        name = director_service.update(did, request.json)
        return DirectorSchema().dump(name)