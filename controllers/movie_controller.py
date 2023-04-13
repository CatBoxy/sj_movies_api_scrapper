from dataclasses import dataclass

from infrastructure.value_objects.datetime import DateTime
from repositories.movie_repo import MovieRepo


@dataclass
class MovieController():
    __repo: MovieRepo

    def saveMovie(self):
        # Manual saving of a movie
        pass

    def getMovie(self, movie_id: str):
        movie = self.__repo.getMovie(movie_id)
        return movie

    def getAllMovies(self, date: str):
        datetime = DateTime(date)
        movies = self.__repo.getAllMovies(datetime.dateTime)
        return movies

    def editMovie(self):
        pass

    def deleteMovie(self):
        pass