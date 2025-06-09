from exceptions.invalid_age_error import InvalidAgeError


class Participant:

    organization = "Python Academy"
    _counter = 1

    def __init__(self, name="John Doe", age="0", gender=""):
        self.name = name
        self.age = age
        self._gender = gender
        self.__id = Participant._counter
        Participant._counter += 1

    def __del__(self):
        print(f"{self.name} is recycled")

    def __str__(self):
        return f"{self.name} age {self.age} gender {self._gender} id {self.__id}"

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def set_age(self, age):
        if age < 8:
            raise InvalidAgeError("Age must be at least 8")
        self.age = age

    @classmethod
    def get_counter(cls):
        return Participant._counter