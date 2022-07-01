import sqlite3, os

# Dictionary Factory to convert sqlite3.Row(tuple) to dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#Sql run query
def runDBQuery(dbpath, query):
    newdbpath = os.getcwd()+'/resources/databank/'+dbpath
    con = sqlite3.connect(newdbpath)
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    return cur.fetchall()

#Paths to databases
users_db = 'users/db.db3'