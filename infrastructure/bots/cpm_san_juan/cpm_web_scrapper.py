import time
from dataclasses import dataclass, field
from typing import Any, List

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from infrastructure.bots.cpm_san_juan.movie_scrapper import CpmMovieScrapper
from infrastructure.bots.scrapper import Scrapper
from infrastructure.value_objects.movie import Movie
from selenium.webdriver.chrome.service import Service


@dataclass
class CpmWebScrapper(Scrapper):
    driver: Any
    options: Any
    driverPath: str
    movies: List[Movie] = field(default_factory=lambda: [])
    url: str = 'https://cpmcines.com/complejo/sanjuan'

    def scrape(self):
        self.driver.get(self.url)
        time.sleep(7)
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'horarios-complejo .row > .col > .row > .col > img')
        urls = []

        for element in elements:
            ActionChains(self.driver).click(element).perform()
            time.sleep(1)
            urls.append(self.driver.current_url)
            self.driver.execute_script("window.history.go(-1)")

        for url in urls:
            service = Service(self.driverPath)
            newDriver = webdriver.Chrome(service=service, options=self.options)
            newDriver.get(url)
            cpmMovie = CpmMovieScrapper(driver=newDriver)
            self.movies.append(cpmMovie)
        return self.movies

    def getMoviesAmount(self) -> int:
        return len(self.movies)
