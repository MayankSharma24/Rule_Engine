import unittest
from ast import Node

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node("operand", value="age")
        self.assertEqual(node.type, "operand")
        self.assertEqual(node.value, "age")

if __name__ == '__main__':
    unittest.main()  # Removed any potential invisible characters here
