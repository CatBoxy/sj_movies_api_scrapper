from dataclasses import dataclass
from typing import List

from infrastructure.db.db import DB


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

    def getMovie(self, movie_id: str):
        movieQuery = "SELECT * FROM movies WHERE movie_id = %s"
        roomsQuery = "SELECT * FROM rooms WHERE movie_id = %s"
        timeQuery = "SELECT * FROM times"
        dbMovie = self.__db.select(
            movieQuery, (movie_id, )
        )
        dbRooms = self.__db.select(
            roomsQuery, (movie_id, )
        )
        dbTimes = self.__db.select(
            timeQuery
        )
        rooms = []
        for dbRoom in dbRooms:
            roomTimes = []
            for dbTime in dbTimes:
                if dbTime["room_id"] == dbRoom["room_id"]:
                    roomTimes.append(dbTime["time"])
            dbRoom["times"] = roomTimes
            rooms.append(dbRoom)
        dbMovie[0]["rooms"] = rooms
        return dbMovie

    def getAllMovieTimes(self, datetime: str):
        timesQuery = "SELECT time, room_name, movie_name, cinema, scrape_date, image_url " \
                      "FROM times INNER JOIN rooms " \
                      "ON times.room_id = rooms.room_id INNER JOIN movies ON rooms.movie_id = movies.movie_id " \
                      "WHERE scrape_date = (SELECT MAX(scrape_date) FROM movies WHERE scrape_date <= %s)"
        times = self.__db.select(timesQuery, (datetime,))
        return times

    def getAllMovies(self, datetime: str):
        moviesQuery = "SELECT * FROM movies " \
                      "WHERE scrape_date = (SELECT MAX(scrape_date) FROM movies WHERE scrape_date <= %s)"
        movies = self.__db.select(moviesQuery, (datetime,))
        return movies

    def editMovie(self):
        pass

    def deleteMovie(self):
        pass
