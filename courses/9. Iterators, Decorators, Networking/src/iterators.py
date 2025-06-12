class Element:
    currentElement = -1
    elements = [4, 5, 1, 2]

    def __next__(self):
        self.currentElement += 1
        if self.currentElement > 3:
            raise StopIteration
        return self.elements[self.currentElement]


class Iterable:
    def __iter__(self):
        return Element()


def main():
    for i in Iterable():
        print(i)


if __name__ == '__main__':
    main()
