def fibonacci():

    current_number, next_number = 0, 1
    while True:
        yield current_number
        current_number, next_number = next_number, current_number + next_number

generator = fibonacci()
for i in range(50):
    print(next(generator))

