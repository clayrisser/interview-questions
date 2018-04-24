from stack import Stack
from unittest import TestCase

class TestStack(TestCase):
  def test_push(self):
    stack = Stack([0])
    stack.push(1)
    self.assertEqual(stack.items, [0, 1])

  def test_pop(self):
    stack = Stack([0, 1])
    popped = stack.pop()
    self.assertEqual(popped, 1)
    self.assertEqual(stack.items, [0])

  def test_peek(self):
    stack = Stack([0, 1])
    self.assertEqual(stack.peek(), 1)
