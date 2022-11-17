from dataclasses import dataclass
from typing import List

from intrastructure.db.db import DB
from intrastructure.value_objects.movie import Movie


@dataclass
class MovieRepo():
    __db: DB

    def saveMovie(self, movieValues: dict, roomValues: List, timeValues: List):
        self.__db.insert('movies', movieValues)
        for room in roomValues:
            self.__db.insert('rooms', room)
        for time in timeValues:
            self.__db.insert('times', time)

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
