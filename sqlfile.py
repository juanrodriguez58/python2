import sqlite3

def inserta(t1, t2, url, com):
    sqlOrder = " INSERT INTO Enlaces (tipo1, tipo2, direccion, comentario) VALUES (?,?,?,?)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(t1,t2,url,com))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def leer():
    conn = sqlite3.connect('enlaces.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Enlaces")
    for fila in cur:
        print(fila)     


