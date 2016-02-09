
def generabase():
	cadena = "<HTML><HEAD> PY GENERATED </HEAD><BODY> XYX </BODY></HTML>"
	return cadena

def insertatexto(texto, codigo):
	cadena = '<P>'
	cadena = cadena + texto + '</P> XYX'
	print(codigo, cadena)
	codigo.replace('XYX', cadena)
	return codigo

def insertalista(lista, codigo):
	cadena = "<P><UL>"
	for linea in lista:
		cadena = cadena + "<LI>" + linea + "</LI>"
	cadena = cadena + "</UL></P> \n XYX"
	codigo.replace("XYX", cadena)
	return codigo

def insertalistaenlaces(lista, codigo):
	cadena = "<P><UL>"
	for linea in lista:
		cadena = cadena + "<LI><A href://' " + linea + "'>" + linea + "</A></LI>"
	cadena = cadena + "</UL></P> \n XYX"
	codigo.replace("XYX", cadena)
	return codigo

def insertalistaimagenes(lista, codigo):
	cadena = "<P><UL>"
	for linea in lista:
		cadena = cadena + "<LI><IMG SRC=' " + linea + "'></LI>"
	cadena = cadena + "</UL></P> \n XYX"
	codigo.replace("XYX", cadena)
	return codigo
