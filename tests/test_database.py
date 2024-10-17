import unittest
import os
import sqlite3
from database import init_db, add_rule

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_rules.db'
        conn = sqlite3.connect(self.db_name)
        conn.close()
        init_db()

    def tearDown(self):
        os.remove(self.db_name)

    def test_add_rule(self):
        add_rule("age > 30")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM rules')
        rules = cursor.fetchall()
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0][1], "age > 30")
        conn.close()

if __name__ == '__main__':  # Corrected to use double underscores
    unittest.main()  # Removed any potential invisible characters here
