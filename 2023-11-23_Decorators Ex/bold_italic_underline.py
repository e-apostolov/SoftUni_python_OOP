def check_action(name):
    function_dict = {
        "make_bold": ("<b>", "</b>"),
        "make_italic": ("<i>", "</i>"),
        "make_underline": ("<u>", "</u>")
    }
    start = function_dict[name][0]
    end = function_dict[name][1]
    return start, end


def make_bold(func):
    name = make_bold.__name__

    def wrapper(*args):
        return f"{check_action(name)[0]}{func(*args)}{check_action(name)[1]}"
    return wrapper


def make_italic(func):
    name = make_italic.__name__

    def wrapper(*args):
        return f"{check_action(name)[0]}{func(*args)}{check_action(name)[1]}"
    return wrapper


def make_underline(func):
    name = make_underline.__name__

    def wrapper(*args):
        return f"{check_action(name)[0]}{func(*args)}{check_action(name)[1]}"
    return wrapper

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
