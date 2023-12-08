from typing import List

from project.band_members.musician import Musician


class Drummer(Musician):

    @property
    def valid_skills(self) -> List:
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
