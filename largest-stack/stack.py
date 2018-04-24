class Stack(object):

  def __init__(self, items):
    if items:
      self.items = items
    else:
      self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.items:
      return None
    return self.items.pop()

  def peek(self):
    if not self.items:
      return None
    return self.items[-1]
