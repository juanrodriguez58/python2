import re

def extrae(tipo, texto):
	lista = []
	try:
		if tipo == "e":
			lista = re.findall('href=".+?"', texto)
		elif tipo == "i":
			lista = re.findall('src=".+?"', texto)
		elif tipo == "s":
			lista = re.findall('http.+?"', texto)
		else:
			print("Tipo incorrecto")
		return lista
	except:
		print("Error al dar de alta el registro")
