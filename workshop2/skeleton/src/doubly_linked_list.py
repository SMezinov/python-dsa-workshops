from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_first(self, value):
        self._insert_before_head(value)

    def add_last(self, value):
        self._insert_after_tail(value)

    def insert_after(self, node, value):
        if node is None:
            raise ValueError('Node cannot be None.')

        if node is self._tail:
            self._insert_after_tail(value)
            return

        new_node = LinkedListNode(value)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self._count += 1

    def insert_before(self, node, value):
        if node is None:
            raise ValueError('Node cannot be None.')

        if node is self._head:
            self._insert_before_head(value)
            return

        new_node = LinkedListNode(value)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self._count += 1

    def remove_first(self):
        if self._count == 0:
            raise ValueError('List is empty.')

        value = self._head.value
        self._head = self._head.next
        self._count -= 1

        if self._count == 0:
            self._tail = None
        else:
            self._head.prev = None

        return value

    def remove_last(self):
        if self._count == 0:
            raise ValueError('List is empty.')

        value = self._tail.value
        self._tail = self._tail.prev
        self._count -= 1

        if self._count == 0:
            self._head = None
        else:
            self._tail.next = None

        return value

    def find(self, value):
        current_node = self._head

        while current_node is not None:
            if current_node.value == value:
                return current_node

            current_node = current_node.next

        return None

    def values(self):
        result = []
        current_node = self._head

        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next

        return tuple(result)

    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)

        if self._count == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._count += 1

    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)

        if self._count == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1