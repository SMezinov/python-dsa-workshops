from src.linked_list_node import LinkedListNode

class LinkedStack:
    def __init__(self):
        self._head = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def is_empty(self):
        return self._count == 0

    def push(self, element):
        new_node = LinkedListNode(element, self._head)
        self._head = new_node
        self._count += 1

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty.')

        value = self._head.value
        self._head = self._head.next
        self._count -= 1

        return value

    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty.')

        return self._head.value
