import sqlite3

# Tabla de Enlaces

def insertaLink(t1, t2, url, com):
    sqlOrder = " INSERT INTO Enlaces (tipo1, tipo2, direccion, comentario) VALUES (?,?,?,?)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(t1,t2,url,com))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def leeLink():
    lista = []
    conn = sqlite3.connect('enlaces.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Enlaces")
    for fila in cur:
        lista.append(fila)
    return lista

def consltaLink(dire):
    lista = []
    sqlOrder = " SELECT * FROM Enlaces WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
        lista.append(('','','No records found',''))
    return lista

def borraLink(dir):
    sqlOrder = " DELETE Enlaces WHERE direccion ='" + dir + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro borrado")
    except:
        return("Error al borrar el registro")

# Tabla de contadores

def creaTabla():
    sqlOrder = "CREATE TABLE cicle (direccion TEXT, tipo TEXT, count1 INTEGER, count2 INTEGER)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Tabla creada")
    except:
        return("Error al insertar el registro")


def borraTabla():
    sqlOrder = "DROP TABLE cicle"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Tabla borrada")
    except:
        return("Error al insertar el registro")

def insertaCount(dire, tipo , c1, c2):
    sqlOrder = " INSERT INTO cicle (direccion, tipo, count1, count2) VALUES (?,?,?,?)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(dire, tipo,c1,c2))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def borraCount(dire):
    sqlOrder = " DELETE cicle WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro borrado")
    except:
        return("Error al borrar el registro")

def actualizaCount1(dire,c1):
    sqlOrder = " UPDATE cicle SET count1=" + c1 + "WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def actualizaCount2(dire,c2):
    sqlOrder = " UPDATE cicle SET count2=" + c2 + "WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def consltaCount1(dire):
    lista = []
    sqlOrder = " SELECT count1 FROM cicle WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
        lista.append(('No records found','',0,0))
    return lista

def consltaCount2(dire):
    sqlOrder = " SELECT count2 FROM cicle WHERE direccion ='" + dire + "'"
    count = 999
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            count = int(fila)
    except:
            count = 0
    return count

def consltaPendientes():
    sqlOrder = "SELECT direccion FROM cicle WHERE count1 = 0"
    lista = []
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
            lista.append("No encuentro registros")
    return lista


def consltaTodos():
    sqlOrder = "SELECT * FROM cicle ORDER BY count2 DESC"
    lista = []
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
            lista.append("No encuentro registros")
    return lista




# Tabla de control

def insertaControl(lab,val):
    sqlOrder = " INSERT INTO Control (label, value) VALUES (?,?)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(lab,val))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def borraControl(lab):
    sqlOrder = " DELETE Control WHERE label ='" + lab + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro borrado")
    except:
        return("Error al borrar el registro")

def actualizaControl(lab,val):
    sqlOrder = " UPDATE Control SET value=" + val + "WHERE label ='" + lab + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def consltaControl(lab):
    lista = []
    sqlOrder = " SELECT value FROM Control WHERE label ='" + lab + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
        lista.append(('','','No records found',''))
    return lista
