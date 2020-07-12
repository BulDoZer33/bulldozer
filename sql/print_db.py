import sqlite3, os


BASE_DIR = os.path.dirname(__file__)
db_path = os.path.join(BASE_DIR, 'sql.db')

db = sqlite3.connect(db_path)
cur = db.cursor()

for i in range(1, 4):
   cur.execute(f'SELECT * FROM users WHERE id = {i}')
   print(cur.fetchone())