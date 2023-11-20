from typing import Dict


class dictionary_iter:

    def __init__(self, dictionary: Dict):
        self.dict_tuple = tuple(dictionary.items())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.dict_tuple):
            raise StopIteration
        index = self.current_index
        self.current_index += 1
        return self.dict_tuple[index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

