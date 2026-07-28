from src.linked_list_node import LinkedListNode

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def is_empty(self):
        return self._count == 0

    def enqueue(self, element):
        new_node = LinkedListNode(element)

        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def dequeue(self):
        if self.is_empty:
            raise ValueError('Queue is empty.')

        value = self._head.value
        self._head = self._head.next
        self._count -= 1

        if self.is_empty:
            self._tail = None

        return value

    def peek(self):
        if self.is_empty:
            raise ValueError('Queue is empty.')

        return self._head.value
