import unittest
from src.stack.list_stack import ListStack
from test_utils import add_to_stack

class ListStack_Should(unittest.TestCase):

    def setUp(self):
        self.stack =  ListStack()
    
    def test_count_returnsZero_whenStackEmpty(self):
        # Act & Assert
        self.assertEqual(0, self.stack.count)

    def test_count_returnsCorrectValue_whenStackNotEmpty(self):
        # Arrange
        add_to_stack(1, 2, 3, stack=self.stack)

        # Act & Assert
        self.assertEqual(3, self.stack.count)

    def test_isempty_returnsTrue_whenStackEmpty(self):
        # Act & Assert
        self.assertTrue(self.stack.is_empty)

    def test_isempty_returnsFalse_whenStackNotEmpty(self):
        # Arrange
        add_to_stack(123, stack=self.stack)
        
        # Act & Assert
        self.assertFalse(self.stack.is_empty)

    def test_peek_raisesError_whenStackIsEmpty(self):
        with self.assertRaises(ValueError):
            self.stack.peek()

    def test_peek_returnsCorrectItem_whenStackIsNotEmpty(self):
        # Arrange
        add_to_stack(1,2,3,4, stack=self.stack)

        # Act & Assert
        self.assertEqual(4, self.stack.peek())

    def test_peek_doesNotRemoveItem(self):
        # Arrange
        add_to_stack(1,2,3,4, stack=self.stack)

        # Act 
        _ = self.stack.peek()
        self.assertEqual(4, self.stack.count)

    def test_pop_raisesError_whenStackIsEmpty(self):
        # Act & Assert
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_pop_returnCorrectItems(self):
        # Arrange
        add_to_stack(1,2,3, stack=self.stack)

        # Act & Assert
        self.assertEqual(3, self.stack.pop())

    def test_pop_removesItem(self):
        # Arrange
        add_to_stack(1,2,3, stack=self.stack)

        # Act
        _ = self.stack.pop()

        self.assertEqual(2, self.stack.count)

    def test_push_addsItems(self):
        # Act
        self.stack.push(123)

        # Assert
        self.assertEqual(1, self.stack.count)