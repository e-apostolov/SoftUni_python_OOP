class Person:

    def __init__(self, name):
        self.name = name
        self.current_index = 0
        self.end_index = len(self.name) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.name[index]


p = Person("Long name")
for letter in p:
    print(letter, end="")

for letter in p:
    print(letter, end="")