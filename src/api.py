from ast import Node

def create_rule(rule_string):
    # Basic parsing logic for demonstration
    # In practice, this should be replaced with a full parser
    if ">" in rule_string:
        left, right = rule_string.split(">")
        return Node("operator", left=Node("operand", value=left.strip()), right=Node("operand", value=int(right.strip())))
    return None

def combine_rules(rules):
    root = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if root is None:
            root = rule_ast
        else:
            # For now, we just replace root; a real implementation would combine properly
            root = Node("operator", left=root, right=rule_ast)
    return root

def evaluate_rule(ast_node, data):
    if ast_node.type == "operator":
        if ast_node.value == ">":
            return data.get(ast_node.left.value) > ast_node.right.value
    return False
