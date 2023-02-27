class GenreService:
    def __init__(self, dao):
        self.dao = dao
    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, gid, data):
        self.dao.update(gid, data)

    def delete(self, gid):
        return self.dao.delete(gid)
