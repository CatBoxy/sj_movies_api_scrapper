import os

from dotenv import load_dotenv
from fastapi import APIRouter
from selenium import webdriver

from config import Settings
from controllers.scrapper_controller import ScrapperController
from infrastructure.bots.cpm_san_juan.cpm_web_scrapper import CpmWebScrapper
from infrastructure.db.db import DB
from repositories.movie_repo import MovieRepo
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

router = APIRouter(
    prefix="/scrape",
    tags=["scrape"],
    responses={404: {"description": "Not found"}},
)

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument("--headless")

setting = Settings()
load_dotenv(setting.Config.env_file)
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
DB_PATH = os.environ.get("DB_PATH")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


@router.get("/cpm")
async def scrapeCPM():
    database = DB(DB_PATH, DB_PASSWORD)
    movieRepo = MovieRepo(database)
    cmpScrapper = CpmWebScrapper(driver, options, CHROME_DRIVER_PATH)
    controller = ScrapperController(movieRepo, cmpScrapper)
    movies = controller.scrapeAllMovies()
    controller.saveMovies(movies)
    return "movies saved successfully"


@router.get("/play")
async def scrapePlay():
    pass


@router.get("/cinemacenter")
async def scrapeCinemacenter():
    pass


@router.get("/all")
async def scrapeAll():
    pass
