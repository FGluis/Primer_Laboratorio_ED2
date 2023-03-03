class Node:
  def __init__(self, leaf=False):
    self.leaf = leaf
    self.keys = []
    self.children = []

  def __str__(self):
    return str(self.keys)