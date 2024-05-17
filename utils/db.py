import sqlite3

class SQLite:
    def __init__(self):
        pass

    def executemany(self, db_file, query, data):
        con = sqlite3.connect(db_file)
        cur = con.cursor()

        cur.executemany(f"{query}", data)

        con.commit()
        con.close()
