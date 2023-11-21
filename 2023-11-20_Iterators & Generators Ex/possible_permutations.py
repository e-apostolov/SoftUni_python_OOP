from typing import List


def possible_permutations(ls: List):
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(len(ls)):
            for perm in possible_permutations(ls[:i] + ls[i + 1:]):
                yield [ls[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]