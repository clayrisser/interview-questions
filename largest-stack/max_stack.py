from stack import Stack

class MaxStack(Stack):
  max_item_i = 0
  max_item = 0

  def __init__(self, items):
    super().__init__(items)
    self.set_max_item()

  def get_max(self):
    if not self.items:
      return None
    return self.items[self.max_item_i]

  def push(self, item):
    super().push(item)
    self.set_max_item(item)

  def pop(self):
    popped = super().pop()
    self.set_max_item()
    return popped

  def set_max_item(self, new_item = None):
    if new_item:
      if new_item > self.max_item:
        self.max_item_i = len(self.items) - 1
        self.max_item = self.items[self.max_item_i]
    else:
      for i in range(len(self.items)):
        item = self.items[i]
        max_item = self.max_item
        if item > max_item:
          self.max_item_i = i
          self.max_item = self.items[self.max_item_i]
