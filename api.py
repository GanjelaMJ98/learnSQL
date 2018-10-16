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
    #print(sql)
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

    #for row in cursor.execute(sql):
        #print(row)
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
    #print(sql)
    #for row in cursor.execute(sql):
        #print(row)
    return sql

def updateMain(NewName,CurrentName, column,main_id):
    if CurrentName == "None":
        CurrentName = "NULL"
    if column == 0:
        print("ERROR UPDATE ID")
        return
    elif column == 1:
        #addName(NewName)
        #sql = "update main SET surname_id = (select surname_id from surname_t where surname = '{1}' ) where main_id = '{1}'".format(NewName, main_id)
        sql = "update surname_t SET surname = '{0}' where surname_id = (select surname_id from surname_t where surname = '{1}')".format(NewName,CurrentName)
    elif column == 2:
        #addSurname(NewName)
        #sql = "update main SET name_id = (select name_id from name_t where name = '{1}' ) where main_id = '{1}'".format(NewName, main_id)
        sql = "update name_t SET name = '{0}' where name_id = (select name_id from name_t where name = '{1}')".format(NewName, CurrentName)
    elif column == 3:
        #addPatron(NewName)
        #sql = "update main SET patron_id = (select patron_id from patron_t where patron = '{1}' ) where main_id = '{1}'".format(NewName, main_id)
        sql = "update patron_t SET patron = '{0}' where patron_id = (select patron_id from patron_t where patron = '{1}')".format(NewName, CurrentName)
    elif column == 4:
        #addStreet(NewName)
        #sql = "update main SET street_id = (select street_id from street_t where street = '{1}' ) where main_id = '{1}'".format(NewName, main_id)
        sql = "update street_t SET street = '{0}' where street_id = (select street_id from street_t where street = '{1}')".format(NewName, CurrentName)
    elif column == 5:
        sql = "update main SET bild = '{0}' where main_id = '{1}'".format(NewName, main_id)
    elif column == 6:
        sql = "update main SET block = '{0}' where main_id = '{1}'".format(NewName, main_id)
    elif column == 7:
        sql = "update main SET appr = '{0}' where main_id = '{1}'".format(NewName, main_id)
    elif column == 1:
        sql = "update main SET number = '{0}' where main_id = '{1}'".format(NewName, main_id)
    cursor.execute(sql)
    conn.commit()
    print("update {0} >> {1} in index {2}".format(CurrentName,NewName,main_id))

    #sql = "update name_t SET name = 'Petro' where name_id = (select name_id from name_t where name = 'Petr')"





def searchOnlySurname():
    list = []
    sql = """SELECT surname FROM surname_t """
    for row in cursor.execute(sql):
        list.append(row[0])
    #print(list)
    return tuple(list)

def searchOnlyName():
    list = []
    sql = """SELECT name FROM name_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    #print(list)
    return tuple(list)

def searchOnlyPatron():
    list = []
    sql = """SELECT patron FROM patron_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    #print(list)
    return tuple(list)

def searchOnlyStreet():
    list = []
    sql = """SELECT street FROM street_t"""
    for row in cursor.execute(sql):
        list.append(row[0])
    #print(list)
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





######NAME
def windowNameLoadTable(name = None):
    list = []
    sql = """SELECT * FROM name_t"""
    if name is not None:
        sql += " WHERE name = '{0}'".format(str(name))
    for row in cursor.execute(sql):
        list.append(row[0])
    return sql
def windowNameIdInMain(id):
    list = []
    sql = "select name_id from main"
    cursor.execute(sql)
    for row in cursor.execute(sql):
        list.append(row[0])
    if list.count(id) == 0:
        return False
    else:
        return True
def windowNameDelete(id):
    sql = "DELETE FROM name_t WHERE `name_id` = '{0}'".format(id)
    if windowNameIdInMain(int(id)) == True:
        print("FOREIGN KEY constraint failed: {0}".format(sql))
        return
    else:
        cursor.execute(sql)
        conn.commit()
        print("windowName: delete id ", id)
def windowNameUpdate(NewName,id):
    sql = "update name_t set name = '{0}' where name_id = '{1}'".format(NewName,id)
    cursor.execute(sql)
    conn.commit()
    print("windowName: update id {0}: {1}".format(id,NewName))
######SURNAME
def windowSurnameLoadTable(surname = None):
    list = []
    sql = """SELECT * FROM surname_t"""
    if surname is not None:
        sql += " WHERE surname = '{0}'".format(str(surname))
    for row in cursor.execute(sql):
        list.append(row[0])
    return sql
def windowSurnameIdInMain(id):
    list = []
    sql = "select surname_id from main"
    cursor.execute(sql)
    for row in cursor.execute(sql):
        list.append(row[0])
    if list.count(id) == 0:
        return False
    else:
        return True
def windowSurnameDelete(id):
    sql = "DELETE FROM surname_t WHERE `surname_id` = '{0}'".format(id)
    if windowSurnameIdInMain(int(id)) == True:
        print("FOREIGN KEY constraint failed: {0}".format(sql))
        return
    else:
        cursor.execute(sql)
        conn.commit()
        print("windowSurname: delete id ", id)
def windowSurnameUpdate(NewName,id):
    sql = "update surname_t set surname = '{0}' where surname_id = '{1}'".format(NewName,id)
    cursor.execute(sql)
    conn.commit()
    print("windowSurname: update id {0}: {1}".format(id,NewName))
######PATRON
def windowPatronLoadTable(patron = None):
    list = []
    sql = """SELECT * FROM patron_t"""
    if patron is not None:
        sql += " WHERE patron = '{0}'".format(str(patron))
    for row in cursor.execute(sql):
        list.append(row[0])
    return sql
def windowPatronIdInMain(id):
    list = []
    sql = "select patron_id from main"
    cursor.execute(sql)
    for row in cursor.execute(sql):
        list.append(row[0])
    if list.count(id) == 0:
        return False
    else:
        return True
def windowPatronDelete(id):
    sql = "DELETE FROM patron_t WHERE `patron_id` = '{0}'".format(id)
    if windowPatronIdInMain(int(id)) == True:
        print("FOREIGN KEY constraint failed: {0}".format(sql))
        return
    else:
        cursor.execute(sql)
        conn.commit()
        print("windowPatron: delete id ", id)
def windowPatronUpdate(NewName,id):
    sql = "update patron_t set patron = '{0}' where patron_id = '{1}'".format(NewName,id)
    cursor.execute(sql)
    conn.commit()
    print("windowPatron: update id {0}: {1}".format(id,NewName))
######STREET
def windowStreetLoadTable(street = None):
    list = []
    sql = """SELECT * FROM street_t"""
    if street is not None:
        sql += " WHERE street = '{0}'".format(str(street))
    for row in cursor.execute(sql):
        list.append(row[0])
    return sql
def windowStreetIdInMain(id):
    list = []
    sql = "select street_id from main"
    cursor.execute(sql)
    for row in cursor.execute(sql):
        list.append(row[0])
    if list.count(id) == 0:
        return False
    else:
        return True
def windowStreetDelete(id):
    sql = "DELETE FROM street_t WHERE `street_id` = '{0}'".format(id)
    if windowStreetIdInMain(int(id)) == True:
        print("FOREIGN KEY constraint failed: {0}".format(sql))
        return
    else:
        cursor.execute(sql)
        conn.commit()
        print("windowStreet: delete id ", id)
def windowStreetUpdate(NewName,id):
    sql = "update street_t set street = '{0}' where street_id = '{1}'".format(NewName,id)
    cursor.execute(sql)
    conn.commit()
    print("windowStreet: update id {0}: {1}".format(id,NewName))



if __name__ == "__main__":

    #updateMain("Sidorenko","Sidoenko",1)

    #addSurname("Ganjela")
    #addStreet("Dubosekovskaya")
    #addPatron("Andreevich")
    #addName("Vlad")

    #addMain("Zvezdin","Tema","Olegovich","Balashiha",66,6,666,6666666666)


    conn.commit()