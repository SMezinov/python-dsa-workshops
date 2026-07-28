class ListQueue:
    def __init__(self):
        self._items = []

    @property
    def count(self):
        return len(self._items)

    @property
    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, element):
        self._items.append(element)

    def dequeue(self):
        if self.is_empty:
            raise ValueError('Queue is empty.')

        return self._items.pop(0)

    def peek(self):
        if self.is_empty:
            raise ValueError('Queue is empty.')

        return self._items[0]
