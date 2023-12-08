from typing import List

from project.band_members.musician import Musician


class Guitarist(Musician):

    @property
    def valid_skills(self) -> List:
        return ["play metal", "play rock", "play jazz"]