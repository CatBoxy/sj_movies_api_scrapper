from dataclasses import dataclass
from typing import List

from intrastructure.bots.scrapper import Scrapper
from intrastructure.value_objects.movie import Movie
from repositories.movie_repo import MovieRepo


@dataclass
class ScrapperController():
    # db: DB
    __repo: MovieRepo
    __bot: Scrapper

    def saveMovie(self, movie: Movie):
        pass

    def saveMovies(self, movies: List[Movie]):
        for movie in movies:
            self.saveMovie(movie)

    def scrapeMovie(self):
        pass

    def scrapeAllMovies(self) -> List[Movie]:
        return self.__bot.scrape()

    def editMovie(self):
        pass
