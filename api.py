import sqlite3

conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()



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
    if bild == "":
        bild = "NULL"
    if block == "":
        block = "NULL"
    if appr == "":
        appr = "NULL"
    if number == "":
        number = "NULL"

    sql = "INSERT INTO main VALUES (NULL, {0},{1},{2},{3},{4},{5},{6},{7})".format(surname_sql,name_sql,patron_sql,street_sql,bild,block,appr,number)
    print(sql)
    cursor.execute(sql)
    conn.commit()


def DeleteByID(id):
    sql = "DELETE FROM main WHERE `main_id` = '{}'".format(id)
    cursor.execute(sql)
    conn.commit()
    print("delete id ", id)




def searchMain(surname = None,name = None,  patron = None, street = None, bild = None,block = None,appr = None,number = None):
    sql = '''SELECT m.main_id,
                    s.surname,
                    n.name,
                    p.patron,
                    st.street,
                    m.bild,
                    m.block,
                    m.appr,
                    m.number
                     FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m '''

    if surname is not None and name is not None and patron is not None and street is not None:
        sql = sql + "WHERE s.surname = '{0}' and n.name = '{1}' and p.patron = '{2}' and st.street = '{3}'".format(surname,name,patron, street)

    for row in cursor.execute(sql):
        print(row)
    return sql

def NEWsearchMain(surname = None,name = None,  patron = None, street = None, bild = None,block = None,appr = None,number = None):
    sql = """SELECT m.main_id,
                    s.surname,
                    n.name,
                    p.patron,
                    st.street,
                    m.bild,
                    m.block,
                    m.appr,
                    m.number
                     FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m """
    sql = sql + "WHERE 1 = 1 "
    if surname != "":
        sql += "AND s.surname = '{0}' ".format(surname)
    if name != "":
        sql += "AND n.name = '{0}' ".format(name)
    if patron != "":
        sql += "AND p.patron = '{0}' ".format(patron)
    if street != "":
        sql += "AND st.street = '{0}' ".format(street)
    if bild != "":
        sql += "AND m.bild = '{0}' ".format(bild)
    if block != "":
        sql += "AND m.block = '{0}' ".format(block)
    if appr != "":
        sql += "AND m.appr = '{0}' ".format(appr)
    if number != "":
        sql += "AND m.number = '{0}' ".format(number)
    print(sql)
    for row in cursor.execute(sql):
        print(row)
    return sql


def searchOnlySurname():
    list = []
    sql = """SELECT surname FROM surname_t """
    for row in cursor.execute(sql):
        list.append(row[0])
    print(list)
    return tuple(list)

def searchOnlyName():
    list = []
    sql = """SELECT name FROM name_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    print(list)
    return tuple(list)

def searchOnlyPatron():
    list = []
    sql = """SELECT patron FROM patron_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    print(list)
    return tuple(list)

def searchOnlyStreet():
    list = []
    sql = """SELECT street FROM street_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    print(list)
    return tuple(list)


def searchSurname(surname):
    sql = """SELECT m.main_id,
                        s.surname,
                        n.name,
                        p.patron,
                        st.street,
                        m.bild,
                        m.block,
                        m.appr,
                        m.number
                         FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m WHERE s.surname = '{0}'""".format(surname)
    #print(sql)
    for row in cursor.execute(sql):
        print(row)
    return sql
def searchName(name):
    sql = """SELECT m.main_id,
                        s.surname,
                        n.name,
                        p.patron,
                        st.street,
                        m.bild,
                        m.block,
                        m.appr,
                        m.number
                         FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m WHERE n.name = '{0}'""".format(name)
    #print(sql)
    for row in cursor.execute(sql):
        print(row)
    return sql
def searchPatron(patron):
    sql = """SELECT m.main_id,
                        s.surname,
                        n.name,
                        p.patron,
                        st.street,
                        m.bild,
                        m.block,
                        m.appr,
                        m.number
                         FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m WHERE p.patron = '{0}'""".format(patron)
    #print(sql)
    for row in cursor.execute(sql):
        print(row)
    return sql
def searchStreet(street):
    sql = """SELECT m.main_id,
                        s.surname,
                        n.name,
                        p.patron,
                        st.street,
                        m.bild,
                        m.block,
                        m.appr,
                        m.number
                         FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m WHERE st.street = '{0}'""".format(street)
    #print(sql)
    for row in cursor.execute(sql):
        print(row)
    return sql

def Name():
    list = []
    sql = """SELECT * FROM name_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    print(list)
    return sql


if __name__ == "__main__":
    Name()
    #addSurname("Ganjela")
    #addStreet("Dubosekovskaya")
    #addPatron("Andreevich")
    #addName("Vlad")
    #addMain("Zvezdin","Tema","Olegovich","Balashiha",66,6,666,6666666666)

    #searchMain()
    #searchMain(surname="Zvezdin")
    #searchMain(surname="Zvezdin", name= "Tema" , patron="Olegovich" , street="Balashiha")
    #searchStreet("Dubosecovskaya")
    searchOnlySurname()

    conn.commit()