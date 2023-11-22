def repeat(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, *kwargs)
            return (result + "\n") * n
        return wrapper
    return decorator


@repeat(4)
def say(word):
    return word


print(say("Hello"))

