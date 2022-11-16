from typing import Union

from fastapi import FastAPI

from routes import movie_router, scrapper_router

app = FastAPI()

app.include_router(movie_router.router)
app.include_router(scrapper_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

