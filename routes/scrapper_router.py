from fastapi import APIRouter
from selenium import webdriver
from controllers.scrapper_controller import ScrapperController
from intrastructure.bots.cpm_san_juan.cpm_web_scrapper import CpmWebScrapper
from intrastructure.db.db import DB
from repositories.movie_repo import MovieRepo

router = APIRouter(
    prefix="/scrape",
    tags=["scrape"],
    responses={404: {"description": "Not found"}},
)

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = 'C:/Users/Chalamardo/dev/python/chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)

@router.get("/cpm")
async def scrapeCPM():
    database = DB('movies_db')
    movieRepo = MovieRepo(database)
    cmpScrapper = CpmWebScrapper(driver, options)
    controller = ScrapperController(movieRepo, cmpScrapper)
    movies = controller.scrapeAllMovies()
    controller.saveMovies(movies)

@router.get("/play")
async def scrapePlay():
    pass


@router.get("/cinemacenter")
async def scrapeCinemacenter():
    pass


@router.get("/all")
async def scrapeAll():
    pass
