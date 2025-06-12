from functools import wraps
import os
from pickle import dump, load, PickleError


def serialize(filename):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                res = function(*args, **kwargs)
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                print("Saving the library object...")
                with open(filename, "wb") as file:
                    dump(res, file)
                print("Library object serialized.")
                return res
            except (OSError, PickleError) as e:
                print(f"Failed to serialize object: {e}")
                return None
        return wrapper
    return decorator


def deserialize(filename):
    def decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            try:
                if not os.path.exists(filename):
                    print(f"File {filename} does not exist. Cannot deserialize.")
                    return None

                print("Loading library object from file...")
                with open(filename, "rb") as file:
                    loaded_object = load(file)

                if hasattr(loaded_object, '__dict__'):
                    self.__dict__.update(loaded_object.__dict__)

                print("Library object deserialized and restored.")

                return function(self, *args, **kwargs)

            except (OSError, PickleError) as e:
                print(f"Failed to deserialize object: {e}")
                return None

        return wrapper

    return decorator
