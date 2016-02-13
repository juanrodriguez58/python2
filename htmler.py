
def generabase():
	cadena = "<HTML><HEAD> PY GENERATED </HEAD><BODY> XYX </BODY></HTML>"
	return cadena
    
def insertatexto(texto, codigo):
	cadena = "<P>" + texto + "</P> \n XYX"
	return codigo.replace('XYX', cadena)

def insertalista(lista, codigo):
    cadena = "<P><UL>"
    for linea in lista:
        if linea !="0":
            cadena = cadena + "<LI>" + linea + "</LI>"
    cadena = cadena + "</UL></P> \n XYX"
    return codigo.replace('XYX', cadena)

def insertalistaenlaces(lista, codigo):
    cadena = "<P><UL>"
    for linea in lista:
            if linea != "0":
                cadena = cadena + "<LI><A href://' " + linea + "'>" + linea + "</A></LI>"
    cadena = cadena + "</UL></P> \n XYX"
    codigo.replace("XYX", cadena)
    return codigo

def insertalistaimagenes(lista, codigo):
    cadena = "<P><UL>"
    for linea in lista:
        if linea != "0":
            cadena = cadena + "<LI><IMG SRC=' " + linea + "'></LI>"
    cadena = cadena + "</UL></P> \n XYX"
    codigo.replace("XYX", cadena)
    return codigo
