def uppercase(n_letters):
    def decorator(function):
        def wrapper():
            result = function()
            upper_part = result[:n_letters].upper()
            lower_part = result[n_letters:]
            return upper_part + lower_part
        return wrapper
    return decorator


@uppercase(1)
def say_hi():
    return 'hello there'


print(say_hi())
