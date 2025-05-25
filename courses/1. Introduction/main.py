def changeValues(value1, value2):
    value1 = "New value"
    value2 = 100
    return


vb1, vb2 = 10, 20
changeValues(vb1, vb2)
print(vb1, vb2)


def doSomething1(list):
    for value in list:
        value = 10
    return


lista = [1, 2, 3, 4, 5]
doSomething1(lista)
print(lista)


def doSomething(value1, value2):
    print("value1 = ", value1)
    print("value2 = ", value2)
    return


# using keywords
doSomething(value1=10, value2=20)
doSomething(value2=20, value1=10)

value = 1


def test():
    global value
    value = 2


test()
print(value)
