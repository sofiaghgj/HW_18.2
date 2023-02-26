class MovieService:
    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, data):
        return self.dao.update(mid, data)

    def delete(self, mid):
        return self.dao.delete(mid)
