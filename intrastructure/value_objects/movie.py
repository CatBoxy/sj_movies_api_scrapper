from dataclasses import dataclass
from typing import List

from intrastructure.room import Room


@dataclass(frozen=True)
class Movie():
    name: str
    cinema: str
    movieRoom: List[Room]
    imageUrl: str = None
