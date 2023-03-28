from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Room():
    name: str
    movieTimes: List[str]

    def getTimes(self) -> List[str]:
        return self.movieTimes
