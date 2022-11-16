import re
from dataclasses import dataclass, field
from typing import Any, List

import unicodedata
from selenium import webdriver
from bs4 import BeautifulSoup

from intrastructure.bots.scrapper import Scrapper
from intrastructure.value_objects.movie import Movie
from intrastructure.value_objects.room import Room


@dataclass
class PlayCinemaWebScrapper(Scrapper):
    driver: Any
    options: Any
    movies: List[Movie] = field(default_factory=lambda: [])
    url: str = 'https://sanjuancultural.com/cartelera-play-cinema-san-juan/'
    driver_path = 'C:/Users/Chalamardo/dev/python/chromedriver.exe'
    hourRegex = "([0-1][0-9]|2[0-3]):[0-5][0-9]"
    roomNameRegex = "(2D Cast|2D Sub|3D Cast|3D Sub)"

    def scrape(self):
        self.driver.get(self.url)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        patternTime = re.compile(self.hourRegex)
        patternRoomName = re.compile(self.roomNameRegex)
        pTags = soup.findAll('p', attrs={'style': "font-weight: 400;"})
        for p in pTags:
            if p.string == '——-':
                break
            movieName = self.getMovieName(p)
            stringArray = self.getMovieTimes(patternTime, p)
            rooms = self.getMovieRooms(patternRoomName, patternTime, stringArray)
            movie = Movie(name=movieName, cinema='Play Cinema San Juan', movieRoom=rooms)
            self.movies.append(movie)
        print(self.movies)

    def getMovieTimes(self, pattern, p) -> List[str]:
        stringArray = []
        for string in p.strings:
            if pattern.search(string) is not None:
                stringArray.append(string)
        return stringArray

    def getMovieName(self, p) -> str:
        strongArray = []
        for strong in p.findAll('strong'):
            for string in strong.strings:
                normalizedStr = unicodedata.normalize("NFKD", string)
                strongArray.append(normalizedStr)
        print(strongArray)
        strongArray = list(reversed(strongArray))
        if len(strongArray) != 0:
            return strongArray[0]

    def getMovieRooms(self, patternRoomName, patternTime, stringArray: List[str]) -> List[Room]:
        roomArray = []
        for string in stringArray:
            roomName = ''
            roomTimeList = []
            nameMatches = patternRoomName.finditer(string)
            timeMatches = patternTime.finditer(string)
            for match in nameMatches:
                roomName = string[match.span()[0]:match.span()[1]]
            for match in timeMatches:
                roomTimeList.append(string[match.span()[0]:match.span()[1]])
            newRoom = Room(roomName, roomTimeList)
            roomArray.append(newRoom)
        return roomArray

    def getMoviesAmount(self) -> int:
        return len(self.movies)


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:/Users/Chalamardo/dev/python/chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

playCinemaScrapper = PlayCinemaWebScrapper(driver=driver, options=options)
playCinemaScrapper.scrape()
