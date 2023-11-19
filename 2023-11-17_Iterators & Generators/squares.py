# option 1:

def squares(n):
    for num in range(1, n + 1):
        current_num = num * num
        yield current_num
        num += 1

print(list(squares(5)))

# option 2:


def squares(n):
    current = 1
    while current <= n:
        yield current * current
        current += 1

print(list(squares(5)))

