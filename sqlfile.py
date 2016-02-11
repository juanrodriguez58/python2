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

def consltaLink(dir):
    sqlOrder = " SELECT * FROM Enlaces WHERE direccion ='" + dir + "'"
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

def insertaCount(dir, c1, c2):
    sqlOrder = " INSERT INTO Counter (direccion, count1, count2) VALUES (?,?,?)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(dir,c1,c2))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def borraCount(dir):
    sqlOrder = " DELETE Counter WHERE direccion ='" + dir + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro borrado")
    except:
        return("Error al borrar el registro")

def actualizaCount1(dir,c1):
    sqlOrder = " UPDATE Counter SET count1=" + c1 + "WHERE direccion ='" + dir + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def actualizaCount2(dir,c2):
    sqlOrder = " UPDATE Counter SET count2=" + c2 + "WHERE direccion ='" + dir + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def consltaCount(dir):
    sqlOrder = " SELECT value FROM Counter WHERE label ='" + dir + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
        lista.append(('','','No records found',''))
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
