import sqlite3

connection = sqlite3.connect('database.db')


with open('trombi_model.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO utilisateur (Utilisateur_Nom, MotDePasse) VALUES (?, ?)",
            ('UserTest', 'UserTest1234')
            )

connection.commit()
connection.close()
