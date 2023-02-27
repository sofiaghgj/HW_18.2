from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters=None):
        return self.dao.get_all(filters=filters)

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, data):
        return self.dao.update(mid, data)

    def delete(self, mid):
        return self.dao.delete(mid)
