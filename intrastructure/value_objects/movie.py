from dataclasses import dataclass
from typing import List

from intrastructure.value_objects.room import Room


@dataclass(frozen=True)
class Movie():
    name: str
    cinema: str
    movieRoom: List[Room]
    imageUrl: str = None

    def getRooms(self) -> List[Room]:
        return self.movieRoom
