from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for page in self.photos:
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {self.photos.index(page) + 1} slot {page.index(label) + 1}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        result = []
        for page in self.photos:
            result.append(separator)
            result.append(" ".join(["[]" for el in page]))
        result.append(separator)
        return "\n".join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

