from functools import reduce


def addition(x, y=1):
    """
    Sum function
    :param x: first value
    :param y: second value
    :return:
    """
    return x + y


result = addition(3, 4)
print(result)

incrementation = addition(7)
print(incrementation)

sum_result = addition(y=7, x=2)
print(sum_result)


def interchange(value1: int, value2: int) -> None:
    aux = value1
    value1 = value2
    value2 = aux


def interchange2(value1, value2):
    return value2, value1


def interchange3(values):
    if len(values) > 1:
        aux = values[0]
        values[0] = values[1]
        values[1] = aux


def total_sales(**author_sales):
    print(author_sales["John"])


a = 5
b = 9
interchange(a, b)
print(a, b)

a, b = interchange2(a, b)
print(a, b)

my_list = [a, b]
interchange3(my_list)
print(my_list)

for z in my_list:
    z = 100

print(my_list)


def multiplication(*values):
    product = 1
    for v in values:
        product *= v
    return product


print(multiplication(1, 2, 3, 4))
total_sales(John=500, Maria=200, George=400)

l = lambda x, y: x**y
print(l(2, 3))

names = ["John", "George", "Maria", "Ana"]
upper_names = list(map(lambda s : s.upper(), names))
print(upper_names)

long_names = list(filter(lambda s : len(s) > 3, names))
print(long_names)

all_names = reduce(lambda n1, n2: n1 + " | " + n2, names)
print(all_names)
