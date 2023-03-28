import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infrastructure.value_objects.movie import Movie
from infrastructure.value_objects.room import Room


def CpmMovieScrapper(driver) -> Movie:
    try:
        moviePoster = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ion-thumbnail > img"))
        )
        time.sleep(2)
        movieTitle = driver.find_element(By.CSS_SELECTOR, 'h1')
        imageSource = moviePoster.get_attribute('src')
        titleText = movieTitle.get_attribute('innerText')
        rooms = getLocations(driver, 'Espacio San Juan')
        movie = Movie(name=titleText, cinema='CPM Cinemas Espacio San Juan', movieRoom=rooms, imageUrl=imageSource)
        return movie
    except TimeoutException:
        print("Loading took too much time!")


def getLocations(driver, location):
    locations = driver.find_elements(By.CSS_SELECTOR, ".swiper-slide.swiper-slide-active > .slide-zoom > .row")
    roomName = ''
    timesList = []
    roomsList = []
    for row in locations:
        cardHeader = row.find_element(By.CSS_SELECTOR, "ion-card > ion-card-header")
        headerText = cardHeader.get_attribute('innerText')
        if headerText == location:
            movieLanguage = row.find_elements(By.CSS_SELECTOR, ".card-content.card-content-md")
            for room in movieLanguage:
                roomName = room.find_element(By.CSS_SELECTOR, ".title.card-title.card-title-md")
                roomNameText = roomName.get_attribute('innerText')
                roomName = roomNameText
                buttons = room.find_elements(By.CSS_SELECTOR, "button")
                for button in buttons:
                    movieTime = button.find_element(By.CSS_SELECTOR, 'span')
                    movieTimeText = movieTime.get_attribute('innerText')
                    timesList.append(movieTimeText)
                roomsList.append(Room(name=roomName, movieTimes=timesList))
    return roomsList
