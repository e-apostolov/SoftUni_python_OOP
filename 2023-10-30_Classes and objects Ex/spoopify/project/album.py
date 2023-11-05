from project.song import Song


class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = []
        for _ in args:
            self.songs.append(_)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        for s in self.songs:
            if s == song:
                return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        details_list = []
        details_list.append(f"Album {self.name}")
        for s in self.songs:
            details_list.append(s.get_info())
        return "\n== ".join(details_list)




