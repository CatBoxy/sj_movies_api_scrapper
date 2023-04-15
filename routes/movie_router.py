import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Form

from config import Settings
from controllers.movie_controller import MovieController
from infrastructure.db.db import DB
from repositories.movie_repo import MovieRepo

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)

setting = Settings()
load_dotenv(setting.Config.env_file)
DB_PATH = os.environ.get("DB_PATH")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


@router.post("/")
async def readMovies(date: str = Form()):
    database = DB(DB_PATH, DB_PASSWORD)
    movieRepo = MovieRepo(database)
    controller = MovieController(movieRepo)
    movies = controller.getAllMovies(date)
    return {"movies": movies}


@router.post("/times")
async def readMoviesTimes(date: str = Form()):
    database = DB(DB_PATH, DB_PASSWORD)
    movieRepo = MovieRepo(database)
    controller = MovieController(movieRepo)
    moviesTimes = controller.getAllMoviesTimes(date)
    return {"movies_times": moviesTimes}


@router.get("/{movie_id}")
async def readMovieId(movie_id: str, date: str = Form()):
    database = DB(DB_PATH, DB_PASSWORD)
    movieRepo = MovieRepo(database)
    controller = MovieController(movieRepo)
    movie = controller.getMovie(date, movie_id)
    return {"movie": movie}
