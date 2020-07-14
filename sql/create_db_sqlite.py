import sqlite3


db = sqlite3.connect('sql.db')
cur = db.cursor()

def create_table_users():
   cur.execute('CREATE TABLE IF NOT EXISTS users('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'chat_id INTEGER NOT NULL,'
               'balance INTEGER NOT NULL,'
               'income_rate INTEGER,'
               'bulldozer_id INTEGER'
               ');')
   db.commit()


def create_table_bulldozer():
   cur.execute('CREATE TABLE IF NOT EXISTS bulldozer('
               'chat_id IN'
               ');')


if __name__ == '__main__':
   create_table_users()
