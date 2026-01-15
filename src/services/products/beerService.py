class BeerService:
    def __init__(self, beerRepository):
        self.repository = beerRepository

    def getAll(self):
        return self.repository
