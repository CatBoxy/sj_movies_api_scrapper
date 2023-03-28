from fastapi import APIRouter

from controllers.movie_controller import MovieController
from infrastructure.db.db import DB
from repositories.movie_repo import MovieRepo

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def readMovies():
    database = DB('sj-movies')
    movieRepo = MovieRepo(database)
    controller = MovieController(movieRepo)
    movies = controller.getAllMovies()
    return {"movies": movies}


@router.get("/{movie_id}")
async def readMovieId(movie_id: str):
    database = DB('sj-movies')
    movieRepo = MovieRepo(database)
    controller = MovieController(movieRepo)
    movie = controller.getMovie(movie_id)
    return {"movie": movie}



