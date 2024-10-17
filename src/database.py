import sqlite3

def init_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rules (
                        id INTEGER PRIMARY KEY,
                        rule_string TEXT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                     )''')
    conn.commit()
    conn.close()

def add_rule(rule_string):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rules (rule_string) VALUES (?)', (rule_string,))
    conn.co
