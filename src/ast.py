class Node:
    def _init_(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # left child
        self.right = right  # right child (only for operators)
        self.value = value  # value for operand nodes (e.g., number or string)

    def _repr_(self):
        return f"Node({self.type}, {self.value}, {self.left}, {self.right})"