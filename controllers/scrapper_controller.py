import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List

import pytz as pytz

from infrastructure.bots.scrapper import Scrapper
from infrastructure.value_objects.datetime import DateTime
from infrastructure.value_objects.movie import Movie
from infrastructure.value_objects.uuid import UUIDValue
from repositories.movie_repo import MovieRepo


@dataclass
class ScrapperController():
    # db: DB
    __repo: MovieRepo
    __bot: Scrapper

    def saveMovie(self, movie: Movie):
        movieId = str(uuid.uuid4())
        scrapeDate = DateTime(datetime.now(tz=pytz.UTC).strftime("%Y-%m-%d %H:%M:%S"))
        movieValues = {
            "movie_id": UUIDValue(movieId).myUuid,
            "name": movie.name,
            "scrape_date": scrapeDate.dateTime,
            "cinema": movie.cinema,
            "image_url": movie.imageUrl
        }
        roomValues = []
        timeValues = []
        for room in movie.movieRoom:
            roomId = str(uuid.uuid4())
            roomData = {
                "room_id": UUIDValue(roomId).myUuid,
                "name": room.name,
                "movie_id": movieId
            }
            roomValues.append(roomData)
            for time in room.movieTimes:
                timeId = str(uuid.uuid4())
                timeData = {
                    "time_id": UUIDValue(timeId).myUuid,
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
