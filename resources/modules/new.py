import sqlite3, os

#open file
def openFile(filepath):
    if os.path.exists(filepath):
        file = open(filepath, "r")
        return file.read()
    else:
        return False

print(openFile(os.getcwd()+'/resources/databank/users/db.db3'))
print(os.getcwd()+'resources/databank/users/db.db3')
