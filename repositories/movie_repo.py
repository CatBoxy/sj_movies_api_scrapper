from dataclasses import dataclass

from intrastructure.db.db import DB


@dataclass
class MovieRepo():
    __db: DB

    def saveMovie(self):
        pass

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