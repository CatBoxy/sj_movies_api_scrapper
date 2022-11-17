import uuid
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
        movieId = str(uuid.uuid4())
        movieValues = {
            "movie_id": movieId,
            "name": movie.name,
            "cinema": movie.cinema,
            "image_url": movie.imageUrl
        }
        roomValues = []
        timeValues = []
        for room in movie.movieRoom:
            roomId = str(uuid.uuid4())
            roomData = {
                "room_id": roomId,
                "name": room.name,
                "movie_id": movieId
            }
            roomValues.append(roomData)
            for time in room.movieTimes:
                timeData = {
                    "time_id": str(uuid.uuid4()),
                    "time": time,
                    "room_id": roomId
                }
                timeValues.append(timeData)
        self.__repo.saveMovie(movieValues, roomValues, timeValues)

    def saveMovies(self, movies: List[Movie]):
        for movie in movies:
            self.saveMovie(movie)

    def scrapeMovie(self):
        pass

    def scrapeAllMovies(self) -> List[Movie]:
        return self.__bot.scrape()

    def editMovie(self):
        pass
