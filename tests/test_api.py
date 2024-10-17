import unittest
from api import create_rule, evaluate_rule
from ast import Node

class TestAPI(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "age > 30"
        ast = create_rule(rule_string)
        self.assertIsInstance(ast, Node)

    def test_evaluate_rule(self):
        rule_string = "age > 30"
        ast = create_rule(rule_string)
        data = {"age": 35}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':  # Corrected to use double underscores
    unittest.main()  # Removed any potential invisible characters here
