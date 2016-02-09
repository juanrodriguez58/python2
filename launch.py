import sys
import textfile
import cadena
import htmler

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

if accion == "s":
        print("buscar: ", nombre, " en la web")
elif accion == "r":
        print("leer: ", nombre, "en disco")
        filas = textfile.leelineas(nombre)
        texto = htmler.insertalista(filas, texto)
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
else:
        print("Accion no definida")

