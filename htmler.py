
def generabase():
	cadena = '<HTML><HEAD> <link rel="stylesheet" type="text/css" href="ppython2.css"></HEAD><BODY><TITLE>PY GENERATED </TITLE> <div class="text"> <H2>Lista</H2> </div> XYX </BODY></HTML>'
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
                cadena = cadena + "<LI><A href=" + linea + ">" + linea + "</A></LI>"
    cadena = cadena + "</UL></P> \n XYX"
    return codigo.replace('XYX', cadena)

def insertalistaimagenes(lista, codigo):
    cadena = '<P><div class="thumb1"><UL>'
    for linea in lista:
        if linea != "0":
            cadena = cadena + "<LI><IMG SRC=" + linea + "></LI>"
    cadena = cadena + "</UL></div></P> \n XYX"
    return codigo.replace('XYX', cadena)

def insertalistathumb(lista, codigo):
    cadena = '<P>'
    n=0
    title = 'Imagen' + n
    for linea in lista:
        if linea != "0":
                cadena = cadena + '<a href="{name}"><IMG class="thumb1" src="{name}" alt="{title}"></a>'.format(name=linea, title=title)
        if n>5:
                n=0
                cadena = cadena + '</P><P> \n'
    cadena = cadena + '</UL></P> \n XYX'
    return codigo.replace('XYX', cadena)

def muestraImagen(codigo, direccion, title):
        cadena = '<P><a href="{name}"><IMG class="thumb1" src="{name}" alt="{title}"></a></p>'.format(name=direccion, title=title)
        
        return codigo.replace('XYX', cadena)
