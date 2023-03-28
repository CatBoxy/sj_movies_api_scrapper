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

    def getAllMovies(self):
        moviesQuery = "SELECT * FROM movies"
        roomsQuery = "SELECT * FROM rooms"
        timeQuery = "SELECT * FROM times"
        dbMovies = self.__db.select(
            moviesQuery
        )
        dbRooms = self.__db.select(
            roomsQuery
        )
        dbTimes = self.__db.select(
            timeQuery
        )
        movies = []
        rooms = []
        for dbRoom in dbRooms:
            roomTimes = []
            for dbTime in dbTimes:
                if dbTime["room_id"] == dbRoom["room_id"]:
                    roomTimes.append(dbTime["time"])
            dbRoom["times"] = roomTimes
            rooms.append(dbRoom)
        for movie in dbMovies:
            movieRooms = []
            for room in rooms:
                if room["movie_id"] == movie["movie_id"]:
                    newRoom = room.copy()
                    del newRoom["movie_id"]
                    movieRooms.append(newRoom)
            movie["rooms"] = movieRooms
            movies.append(movie)
        return movies

    def editMovie(self):
        pass

    def deleteMovie(self):
        pass
