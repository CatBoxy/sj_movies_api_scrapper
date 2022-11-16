from fastapi import APIRouter

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def readMovies():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{movie_id}")
async def readMovieId():
    return {"username": "fakecurrentuser"}



