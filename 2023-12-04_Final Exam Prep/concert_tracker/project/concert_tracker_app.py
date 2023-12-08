from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    VALID_CONCERT_TYPES = {
        "Rock": {"Drummer": ["play the drums with drumsticks"],
                 "Singer": ["sing high pitch notes"],
                 "Guitarist": ["play rock"]},
        "Metal": {"Drummer": ["play the drums with drumsticks"],
                  "Singer": ["sing low pitch notes"],
                  "Guitarist": ["play metal"]},
        "Jazz": {"Drummer": ["play the drums with drum brushes"],
                 "Singer": ["sing high pitch notes", "sing low pitch notes"],
                 "Guitarist": ["play jazz"]},
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if len(self.musicians) > 0:
            if name in [x.name for x in self.musicians if self.musicians]:
                raise Exception(f"{name} is already a musician!")
        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if len(self.bands) > 0:
            if name in [x.name for x in self.bands]:
                raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((x for x in self.musicians if x.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        band = next((x for x in self.bands if x.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((x for x in self.bands if x.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        musician = next((x for x in band.members if x.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(x for x in self.bands if x.name == band_name)
        for musician in self.VALID_MUSICIAN_TYPES:
            if musician not in [x.__class__.__name__ for x in band.members]:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(x for x in self.concerts if x.place == concert_place)
        members_list = self.VALID_CONCERT_TYPES[concert.genre]
        for member in members_list:
            for skill in members_list[member]:
                member_skills = next(x.skills for x in band.members if x.__class__.__name__ == member)
                if skill not in member_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."














