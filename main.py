import os
from typing import Union

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from config import Settings
from routes import movie_router, scrapper_router

app = FastAPI()

app.include_router(movie_router.router)
app.include_router(scrapper_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8010)), reload=True, log_level="info")
