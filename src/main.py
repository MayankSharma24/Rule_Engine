from database import init_db
from api import create_rule, evaluate_rule

def main():
    init_db()
    rule = "age > 30"
    ast = create_rule(rule)
    data = {"age": 35}
    result = evaluate_rule(ast, data)
    print(f"Rule evaluation result: {result}")

if __name__ == "__main__":  # Corrected to use double underscores
    main()
