import sqlite3

conn = sqlite3.connect("magazin.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produse (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nume TEXT  NOT NULL,
        pret REAL NOT NULL,
        cantitate INTEGER NOT NULL
    )
''')

cursor.execute("INSERT INTO produse (nume, pret, cantitate) VALUES ('peste', 15.0, 10)")
cursor.execute("INSERT INTO produse (nume, pret, cantitate) VALUES ('salam', 15.0, 10)")
conn.commit()
conn.close()
print("Baza de date a fost creata !")