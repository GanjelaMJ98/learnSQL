import sqlite3

conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()

print("Listing:")
for row in cursor.execute("SELECT * from main"):
    print(row)

def addName(name):
    n = False
    for row in cursor.execute("SELECT * from name_t"):
        if row[1] == name:
            n = True
    if n == False:
        cursor.execute("INSERT INTO name_t VALUES (NULL,?) ", [name] )
        print("Added name ", name)
        return 1
    else:
        print("Name already exists")
        return 0

def addSurname(surname):
    n = False
    for row in cursor.execute("SELECT * from surname_t"):
        if row[1] == surname:
            n = True
    if n == False:
        cursor.execute("INSERT INTO surname_t VALUES (NULL,?) ", [surname] )
        print("Added surname ", surname)
        return 1
    else:
        print("Surname already exists")
        return 0

def addStreet(street):
    n = False
    for row in cursor.execute("SELECT * from street_t"):
        if row[1] == street:
            n = True
    if n == False:
        cursor.execute("INSERT INTO street_t VALUES (NULL,?) ", [street] )
        print("Added street ", street)
        return 1
    else:
        print("Street already exists")
        return 0


def addPatron(patron):
    n = False
    for row in cursor.execute("SELECT * from patron_t"):
        if row[1] == patron:
            n = True
    if n == False:
        cursor.execute("INSERT INTO patron_t VALUES (NULL,?) ", [patron])
        print("Added patron ", patron)
        return 1
    else:
        print("Patron already exists")
        return 0


def addMain(surname = None,name = None,  patron = None, street = None, bild = None,block = None,appr = None,number = None):
    addSurname(surname)
    addName(name)
    addPatron(patron)
    addStreet(street)

    surname_sql = "(SELECT surname_id FROM surname_t WHERE surname =  '{0}')".format(surname)
    name_sql = "(SELECT name_id FROM name_t WHERE name =  '{0}')".format(name)
    patron_sql = "(SELECT patron_id FROM patron_t WHERE patron =  '{0}')".format(patron)
    street_sql = "(SELECT street_id FROM street_t WHERE street =  '{0}')".format(street)

    sql = "INSERT INTO main VALUES (NULL, {0},{1},{2},{3},{4},{5},{6},{7})".format(surname_sql,name_sql,patron_sql,street_sql,bild,block,appr,number)
    print(sql)
    cursor.execute(sql)


if __name__ == "__main__":
    #addSurname("Ganjela")
    #addStreet("Dubosekovskaya")
    #addPatron("Andreevich")
    #addName("Vlad")
    addMain("Ganjela","Pavel","Andreevich","Dubosecovskaya",13,2,1415,89017014147)
    conn.commit()