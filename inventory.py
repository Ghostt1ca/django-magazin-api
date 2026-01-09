import sqlite3

conn = sqlite3.connect("magazin.db", check_same_thread=False)
cursor = conn.cursor()

class Produs:
    def __init__(self, nume, pret, cantitate):
        self.nume = nume
        self.pret = pret
        self.cantitate = cantitate

    def la_dict(self):
        return {"nume": self.nume, "pret": self.pret, "cantitate": self.cantitate}

class InventoryManager:
    def __init__(self):
        cursor.execute("SELECT * FROM produse")
        val = cursor.fetchall()
        self.produse = self._incarca_datele(val)

    def getData(self):
        cursor.execute("SELECT * FROM produse")
        val = cursor.fetchall()
        return [Produs(x[1], x[2], x[3]) for x in val]
    
    def _incarca_datele(self, data):
        finalData = [None] * len(data)
        k = 0
        for x in data:
            finalData[k] = {
                "nume": x[1],
                "pret": x[2],
                "cantitate": x[3]
            }
            k += 1
        return [Produs(**d) for d in finalData]

    def adauga(self, nume, pret, cantitate):
        try:
            cursor.execute("INSERT INTO produse (nume, pret, cantitate) VALUES (?, ?, ?)", (nume, pret, cantitate))
            conn.commit()
            return True
        except:
            return False
    
    def vinde(self, nume_produs, unitati):
        cursor.execute("SELECT cantitate FROM produse WHERE nume = ?", (nume_produs,))
        result = cursor.fetchone()
        if result and result[0] >= unitati:
            noua_cantitate = result[0] - unitati
            cursor.execute("UPDATE produse SET cantitate = ? WHERE nume = ?", (noua_cantitate, nume_produs))
            conn.commit()
            return True
        return False
    def sterge(self, id):
        cursor.execute("SELECT nume FROM produse WHERE id = ?", (id,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM produse WHERE id = ?", (id,))
            conn.commit()
            return True
        else:
            return False
    def actualizeaza_pret(self, id, pret):
        cursor.execute("SELECT nume FROM produse WHERE id = ?", (id,))
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE produse SET pret = ? WHERE id = ?", (pret, id))
            conn.commit()
            return True
        else:
            return False