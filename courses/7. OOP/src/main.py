from models.participant import Participant
from models.event import Event


if __name__ == '__main__':
    print("OOP implementations")
    john = Participant("John", 10, "Male")
    alice = Participant()

    print(john.name, john.age, john._gender)
    print(john.__dict__)
    print(john.name, john.age, john._gender, john._Participant__id)
    print(alice.name, alice.age, alice._gender)
    john.company = "Cegeka"
    print(john.__dict__)
    print(alice.__dict__)

    # test __str__
    print(john)
    print(alice)

    python_course = Event("Python Course", "Cegeka")

    print(str(python_course))
    print(python_course._Event__id)
    # print(python_course.__dict__)
    # python_course.ticketPrice = 100

    # test atribute statice
    print(john.organization)
    print(Participant.organization)
    print(alice.organization)

    Participant.organization = "Cegeka"

    print(john.organization)
    print(Participant.organization)
    print(alice.organization)

    john.organization = "None"

    print(john.organization)
    print(Participant.organization)
    print(alice.organization)

    john.set_age(23)
    print(john.get_gender())

    # test destructor
    john = None
    print("End")

    print(Participant.get_counter())
