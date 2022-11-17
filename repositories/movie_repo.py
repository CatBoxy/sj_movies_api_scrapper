from dataclasses import dataclass

from intrastructure.db.db import DB
from intrastructure.value_objects.movie import Movie


@dataclass
class MovieRepo():
    __db: DB

    def saveMovie(self, movie: Movie):

    def saveMovies(self):
        pass

    def getMovie(self):
        pass

    def getAllMovies(self):
        pass

    def editMovie(self):
        pass

    def deleteMovie(self):
        pass