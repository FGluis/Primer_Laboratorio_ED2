class Node:
	def __init__(self, value: list) -> None:
		self.value = value[0]
		self.name = value[1]
		self.left = None
		self.right = None
		self.height = 1
