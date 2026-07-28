import unittest
from src.queue.linked_queue import LinkedQueue
from test_utils import add_to_queue

class LinkedQueue_Should(unittest.TestCase):

    def setUp(self):
        self.queue = LinkedQueue()

    def test_count_returnsZero_whenQueueEmpty(self):
        # Act & Assert
        self.assertEqual(0, self.queue.count)

    def test_count_returnsCorrectValue_whenQueueNotEmpty(self):
        # Arrange
        add_to_queue(1, 2, 3, queue=self.queue)

        # Act & Assert
        self.assertEqual(3, self.queue.count)

    def test_isempty_returnsTrue_whenQueueEmpty(self):
        # Act & Assert
        self.assertTrue(self.queue.is_empty)

    def test_isempty_returnsFalse_whenQueueNotEmpty(self):
        # Arrange
        add_to_queue(123, queue=self.queue)

        # Act & Assert
        self.assertFalse(self.queue.is_empty)

    def test_peek_raisesError_whenQueueIsEmpty(self):
        with self.assertRaises(ValueError):
            self.queue.peek()

    def test_peek_returnsCorrectItem_whenQueueIsNotEmpty(self):
        # Arrange
        add_to_queue(1,2,3,4, queue=self.queue)

        # Act & Assert
        self.assertEqual(1, self.queue.peek())

    def test_peek_doesNotRemoveItem(self):
        # Arrange
        add_to_queue(1,2,3,4, queue=self.queue)

        # Act 
        _ = self.queue.peek()
        self.assertEqual(4, self.queue.count)

    def test_dequeue_raisesError_whenQueueIsEmpty(self):
        # Act & Assert
        with self.assertRaises(ValueError):
            self.queue.dequeue()

    def test_dequeue_returnCorrectItems(self):
        # Arrange
        add_to_queue(1,2,3, queue=self.queue)

        # Act & Assert
        self.assertEqual(1, self.queue.dequeue())

    def test_dequeue_removesItem(self):
        # Arrange
        add_to_queue(1,2,3, queue=self.queue)

        # Act
        _ = self.queue.dequeue()

        self.assertEqual(2, self.queue.count)

    def test_enqueue_addsItems(self):
        # Act
        self.queue.enqueue(123)

        # Assert
        self.assertEqual(1, self.queue.count)