import sys
import textfile
import cadena
import htmler
import web
import beautifuler

def guardar(texto):
        sn = input("Quiere guardar el resultado (S/N) \n")
        if sn == "S":
                archivo = input("Incluya el nombre del fichero \n")
                textfile.escribe (archivo, texto)
                return("archivo guardado")
        else:
                return("fin")
        
# Script de prueba para lanzar las llamadas a las funciones

nombre = sys.argv[2]
accion = sys.argv[1]
filas = []
listaImagen = []
listaEnlace = []
listaOtros = []

if accion == "-s":
        print("buscar: ", nombre, " en la web")
        salida = htmler.generabase()
        enlace = web.getUrl(nombre)
        texto = enlace[1]
        server = enlace [0]
        print("Texto",  texto)
        filas = cadena.extrae(texto)
        for fila in filas:
            t2 = beautifuler.arregla(fila, server)    
            if t2[1] == 'link': 
                listaEnlace.append(t2[0])
            elif t2[1] == "linx":
                listaEnlace.append(t2[0])
            elif t2[1] == "img":
                listaImagen.append(t2[0])
            else:
                listaOtros.append(t2[0])
        print("Lista de salidas")
        salida = htmler.insertatexto("Enlaces", salida)
        salida = htmler.insertalistaenlaces(listaEnlace, salida)
        salida = htmler.insertatexto("Imagenes",  salida)
        salida = htmler.insertalistaimagenes(listaImagen, salida)
        salida = htmler.insertatexto("Otros",  salida)
        salida = htmler.insertalista(listaOtros, salida)
        print(guardar(salida))
elif accion == "r":
        print("leer: ", nombre, "en disco")
        filas = textfile.leelineas(nombre)
        texto = htmler.insertaEnlaces(filas, texto)
        print(texto)
        print(guardar(texto))
elif accion == "b":
        salida = htmler.generabase()
        texto = textfile.leefichero(nombre)
        filas = cadena.extrae("e",texto)
        salida = htmler.insertalista(filas, salida)
        print(salida)
        print(guardar(salida))
elif accion == "h":
        texto = htmler.generabase()
        otro = input("inserta un texto: \n")
        texto = htmler.insertatexto(otro, texto)
        print(texto)
        print(guardar(texto))
elif accion == "-b":
    t = beautifuler.arregla(nombre, "http://www.google.com")
    print(t[0], t[1])
else:
        print("Accion no definida")

