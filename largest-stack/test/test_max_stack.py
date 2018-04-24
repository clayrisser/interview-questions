from max_stack import MaxStack
from unittest import TestCase

class TestMaxStack(TestCase):
  def test_push(self):
    stack = MaxStack([0])
    stack.push(1)
    self.assertEqual(stack.items, [0, 1])

  def test_pop(self):
    stack = MaxStack([0, 1])
    popped = stack.pop()
    self.assertEqual(popped, 1)
    self.assertEqual(stack.items, [0])

  def test_peek(self):
    stack = MaxStack([0, 1])
    self.assertEqual(stack.peek(), 1)

  def test_get_max(self):
    stack = MaxStack([4, 2, 0, 8])
    self.assertEqual(stack.get_max(), 8)
