from dataclasses import dataclass

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

    def getAllMovies(self):
        movies = self.__repo.getAllMovies()
        return movies

    def editMovie(self):
        pass

    def deleteMovie(self):
        pass