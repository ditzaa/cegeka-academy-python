from datetime import datetime
from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Function " + function.__name__ + " called at " + str(datetime.now()))
        function(*args, **kwargs)
    return wrapper


@logger
def add_todo(todo: str):
    print("Added TODO: ", todo)


if __name__ == '__main__':
    add_todo("Do homework")
