from abc import ABC
from dataclasses import dataclass


@dataclass
class Scrapper(ABC):
    def scrape(self):
        raise NotImplemented('not implemented')