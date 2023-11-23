def even_parameters(func):
    def wrapper(*args):
        if any(el for el in args if not isinstance(el, int) or el % 2 != 0):
            return "Please use only even numbers!"
        return func(*args)
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

