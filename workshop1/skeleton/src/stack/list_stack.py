class ListStack:
    def __init__(self):
        self._items = []

    @property
    def count(self):
        return len(self._items)

    @property
    def is_empty(self):
        return len(self._items) == 0

    def push(self, element):
        self._items.append(element)

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty.')

        return self._items.pop()

    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty.')

        return self._items[-1]
