def validate_name(num_line, name):
    """
    Validates that the name has at least 2 characters and only valid characters.
    Allowed characters: letters, spaces, apostrophes ('), hyphens (-) and periods (.).
    """
    if len(name) < 2:
        raise ValueError("name '" + name + "' at the line " + str(num_line + 1) + " in the CSV file is too short.")
    for c in name:
        if not c.isalpha() and c not in [" ", "'", "-", "."]:
            raise ValueError("Name '" + name + "' at the line " + str(num_line + 1) +
                             " in the CSV file has invalid characters.")


def validate_age(num_line, age):
    """
    Validates that the age is an integer between 0 and 200.
    """
    if age < 0 or age > 200:
        raise Exception("Age '" + str(age) + "' at the line " + str(num_line + 1)
                        + " in the CSV file is not in a valid range.")


def validate_grade(num_line, grade):
    """
    Validates that the grade is a float between 0.0 and 10.0.
    """
    if grade < 0.0 or grade > 10.0:
        raise Exception("Grade '" + str(grade) + "' at the line " + str(num_line + 1) +
                        " in the CSV file is not in the valid range (0.00, 10.00).")


def read_students(filename):
    """
    Reads student data from a CSV file.
    :param filename: str - The name of the CSV file
    :return: list of strings - Each string represents a student's data line
    :raises Exception: If the file is empty or cannot be opened
    """
    try:
        with open(filename, "r") as input_file:
            students_data = input_file.readlines()
            if len(students_data) < 1:
                raise Exception("CSV file is empty")
            return students_data
    except FileNotFoundError as error:
        print("File Not Found Error: " + str(error))
    except PermissionError:
        print("Permission denied while trying to read the file.")
    except IOError as error:
        print("IO Error: " + str(error))
    except Exception as error:
        print(str(error))
        return []


def parse_students_data(students_data):
    """
    Parses students' data from list of strings.
    Each line is converted to a tuple (name, age, grade) and added to the result list.
    If a row has invalid or missing data, the parsing is stopped and an empty list is returned.
    :param students_data: list of strings representing students' data
    :return: list of tuples - Each tuple represents data about a student in the format (name, age, grade)
    """
    students = []
    for num_line, line in enumerate(students_data):
        try:
            parts = [p.strip() for p in line.strip().split(",")]

            if len(parts) != 3:
                print(f"Error at line {num_line + 1} in CSV file: Expected 3 fields,"
                      f" got {len(parts)}: '{line.strip()}'")
                return []

            name, age, grade = parts

            try:
                if not name:
                    raise ValueError("The name is missing.")
                validate_name(num_line, name)
            except Exception as e:
                print(f"Error at line {num_line + 1} in CSV file: {e}")
                return []

            try:
                age = int(age)
                validate_age(num_line, age)
            except ValueError:
                print(f"Error at line {num_line + 1} in CSV file: Age '{str(age)}' is not a valid integer.")
                return []
            except Exception as e:
                print(f"Error at line {num_line + 1} in CSV file: {e}")
                return []
            try:
                grade = float(grade)
                validate_grade(num_line, grade)
            except ValueError:
                print(f"Error at the line {num_line + 1} in the CSV file: Grade '{str(grade)}' is not a valid float.")
                return []
            except Exception as e:
                print(f"Error at the line {num_line + 1} in CSV file: {e}")
                return []

            students.append((name, age, grade))
        except Exception as error:
            print("Error: " + str(error))

    return students


def get_average_age(students):
    """
    Calculates the average age of the students.
    :param students: list of tuples - Each tuple represents data about a student in the format (name, age, grade)
    :return: float - average of the students age
    """
    try:
        if not students:
            return "NA"
        ages_sum = 0
        for student in students:
            ages_sum += student[1]
        average = round(ages_sum / len(students), 2)
        return average
    except Exception as error:
        print("Error: " + str(error))


def get_highest_grade(students):
    """
    Determines the highest grade amongst the students.
    :param students: list of tuples - Each tuple represents data about a student in the format (name, age, grade)
    :return: float - the highest grade
    """
    try:
        if not students:
            return "NA"
        highest = -1.00
        for student in students:
            if highest < student[2]:
                highest = student[2]
        return highest
    except Exception as error:
        print("Error: " + str(error))


def get_students_with_lowest_grade(students):
    """
    Determines the student(s) that has(have) the lowest grade.
    :param students: list of tuples - Each tuple represents data about a student in the format (name, age, grade)
    :return: list of tuples in the format (name, grade)
    """
    try:
        if not students:
            return "NA"
        lowest = 11.00
        lowest_students = []
        for name, age, grade in students:
            if lowest > grade:
                lowest_students = []
                lowest = grade
            if lowest >= grade:
                lowest_students.append((name, grade))

        return lowest_students

    except Exception as error:
        print("Error: " + str(error))


def get_passing_rate(students):
    """
    Determines the passing rate (percentage of students with grades greater or equal than 5).
    :param students: list of tuples - Each tuple represents data about a student in the format (name, age, grade)
    :return: float - the passing rate percentage
    """
    try:
        if not students:
            return "NA"
        nb_of_passing_students = 0
        for student in students:
            if student[2] >= 5:
                nb_of_passing_students += 1

        rate = round(100 * nb_of_passing_students / len(students), 2)
        return rate
    except Exception as error:
        print("Error: " + str(error))


def generate_analysis(students):
    """
    Generates a text file named 'analysis.txt' representing a report about the students.
    The analysis contains:
        - the average age of the students;
        - the highest grade of the students;
        - the student(s) with the lowest grade;
        - the passing rate of the students.
    :param students: list of tuples - Each tuple represents data about a student in the format (name, age, grade)
    """
    try:
        with open("analysis.txt", "w") as text_file:
            if not students:
                text_file.write("Student data is unavailable or incorrect")
                raise Exception("Student data is unavailable or incorrect")

            text_file.write("The analysis of the students" + "\n\n")

            avg_age = get_average_age(students)
            text_file.write("Average age of the students: " + str(avg_age) + "\n")
            text_file.write("-----------------------------" + "\n")

            highest_grade = get_highest_grade(students)
            text_file.write("Highest grade amongst the students: " + str(highest_grade) + "\n")
            text_file.write("-----------------------------" + "\n")

            lowest_students = get_students_with_lowest_grade(students)
            text_file.write("Students with the lowest grade:\n")
            for name, grade in lowest_students:
                text_file.write(name + " - " + str(grade) + "\n")
            text_file.write("-----------------------------" + "\n")

            passing_rate = get_passing_rate(students)
            text_file.write("Passing rate: " + str(passing_rate) + "%" + "\n")
            text_file.write("-----------------------------" + "\n")

    except IOError as error:
        print("Error: " + str(error))
    except Exception as error:
        print("Error: " + str(error))


if __name__ == "__main__":
    data = read_students("students.csv")
    students_list = parse_students_data(data)
    print(students_list)
    average_age = get_average_age(students_list)
    print("Average age of the students: " + str(average_age))
    highest_grade = get_highest_grade(students_list)
    print("Highest grade among the students: " + str(highest_grade))
    lowest_students = get_students_with_lowest_grade(students_list)
    print("Students with the lowest grade: " + str(lowest_students))
    passing_rate = get_passing_rate(students_list)
    print("Passing rate: " + str(passing_rate) + "%")
    generate_analysis(students_list)
