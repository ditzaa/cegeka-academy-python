import datetime


def log(message):
    try:
        log_file = open("logs.txt", "a")
        timestamp = datetime.datetime.now()
        log_file.write(str(timestamp) + " - " + message + "\n")
        log_file.close()
    except IOError as error:
        print("Error: " + str(error))


def validate_name(name):
    if len(name) < 2:
        raise Exception("Invalid name")


def get_name():
    while True:
        try:
            name = input("Enter your name: ")
            validate_name(name)
            return name
        except Exception:
            print("Invalid name")


def register_participant():
    while True:
        try:
            name = get_name()
            validate_name(name)
            age = int(input("Enter your age: "))
            return (name, age)
        except ValueError:
            print("Invalid age")
        except Exception as e:
            print(str(e))
        finally:
            print("Not needed")


def import_participants(filename):
    new_participants = []
    try:
        with open(filename, "r") as input_file:
            participants = input_file.readlines()
            for participant in participants:
                name, age, *_ = participant.strip().split(",")
                new_participants.append((name, age))
    except FileNotFoundError as error:
        print("File not found Error: " + str(error))
    except IOError as error:
        print("IO Error: " + str(error))
    except Exception as error:
        print(str(error))
    return new_participants


def test_binary_files(participant):
    bin_file = open("participant.bin", "wb")
    bin_file.write(participant[0].encode("utf-8"))
    bin_file.write(int.to_bytes(participant[1], 4, byteorder="little"))
    bin_file.close()


if __name__ == "__main__":
    log("Start registration session")
    participant = register_participant()
    print(participant)
    new_participants = import_participants("participants.txt")
    print(new_participants)

    test_binary_files(participant)
    log("End registration session")
