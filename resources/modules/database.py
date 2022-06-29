import sqlite3, os

# Dictionary Factory
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#Sql run query
def runQuery(dbpath, query):
    con = sqlite3.connect("C:/Users/Student/Desktop/Ylearn/resources/databank/db.db3")
    con.row_factory = dict_factory
    cur = con.cursor()
    print(query)
    cur.execute(query)
    con.commit
    return cur.fetchall()