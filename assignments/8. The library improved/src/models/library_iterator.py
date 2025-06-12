class LibraryIterator:
    def __init__(self, books):
        self._books = list(books.values())
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= len(self._books):
            raise StopIteration
        current_element = self._books[self._current_index]
        self._current_index += 1
        return current_element
