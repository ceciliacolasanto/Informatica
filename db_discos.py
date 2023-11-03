import sqlite3
DISCOS_DB = "discos.db"


def get_db():
    conn = sqlite3.connect(DISCOS_DB)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                artista TEXT NOT NULL,
                precio REAL NOT NULL,
                fecha INTEGER NOT NULL,
                idioma TEXT NOT NULL,
                n_canciones INTEGER NOT NULL,
                genero TEXT NOT NULL,
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)