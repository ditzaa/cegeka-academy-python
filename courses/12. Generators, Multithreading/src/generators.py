def fib(max_value):
    a, b = 0, 1
    while a < max_value:
        yield a
        a, b = b, a + b


def generate_square():
    while True:
        x = yield
        yield x ** 2


if __name__ == '__main__':

    fib_generator = fib(50)
    print(type(fib_generator))
    for value in fib_generator:
        # other logic
        print(value)

    print("---")
    square = generate_square()
    square.__next__()
    for i in range(1, 6):
        y = square.send(i)
        square.__next__()
