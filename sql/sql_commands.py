import sqlite3, os


BASE_DIR = os.path.dirname(__file__)
db_path = os.path.join(BASE_DIR, 'sql.db')

db = sqlite3.connect(db_path)
cur = db.cursor()

def user_add_for_db(chat_id: int):
   cur.execute(f'SELECT chat_id FROM users WHERE chat_id = {chat_id}')

   if cur.fetchone() == None:
      cur.execute('INSERT INTO users(chat_id, balance) VALUES(?, ?)', (chat_id, 500))
      db.commit()

def getting_balance(chat_id: int):
   cur.execute(f'SELECT balance FROM users WHERE chat_id = {chat_id}')

   return cur.fetchone()[0]

def change_of_balance(chat_id: int, sum: int):
   cur.execute(f'SELECT balance FROM users WHERE chat_id = {chat_id}')
   cur.execute(f'UPDATE users SET balance = {cur.fetchone()[0] + sum} WHERE chat_id = {chat_id}')
   db.commit()

