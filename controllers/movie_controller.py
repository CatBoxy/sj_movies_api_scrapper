from dataclasses import dataclass

from infrastructure.value_objects.datetime import DateTime
from repositories.movie_repo import MovieRepo


@dataclass
class MovieController():
    __repo: MovieRepo

    def saveMovie(self):
        # Manual saving of a movie
        pass

    def getMovie(self, datetime: str, movie_id: str):
        # TODO Continue with movie dict, it will remain as a dict
        rows = self.__repo.getMovie(datetime, movie_id)
        movie = {
            "movie_name": rows[0]["movie_name"],

        }
        return movie

    def getAllMoviesTimes(self, date: str):
        datetime = DateTime(date)
        movies = self.__repo.getAllMoviesTimes(datetime.dateTime)
        return movies

    def getAllMovies(self, date: str):
        datetime = DateTime(date)
        movies = self.__repo.getAllMovies(datetime.dateTime)
        return movies

    def editMovie(self):
        pass

    def deleteMovie(self):
        pass