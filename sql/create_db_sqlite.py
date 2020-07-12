import sqlite3


def create_db():
   db = sqlite3.connect('sql.db')
   cur = db.cursor()

   cur.execute('CREATE TABLE IF NOT EXISTS users('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'chat_id INTEGER NOT NULL,'
               'balance INTEGER NOT NULL,'
               'income_rate INTEGER,'
               'bulldozer_id INTEGER'
               ');')
   db.commit()


if __name__ == '__main__':
   create_db()
