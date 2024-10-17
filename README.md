# Rule_Engine

## Overview
This project is a simple 3-tier rule engine application that determines user eligibility based on various attributes using an Abstract Syntax Tree (AST) to represent rules.

## Features
- Dynamic rule creation and evaluation
- Rule storage using SQLite
- Basic error handling and validation

## Installation

1. Clone the repository:
   ```bash```
   git clone <repository-url>
   cd rule_engine
2. Install dependencies:
   pip install -r requirements.txt
3. Initialize the database: 
   python -c "from src.database import init_db; init_db()"
