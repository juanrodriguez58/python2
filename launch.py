import sys
import textfile
import cadena


nombre = sys.argv[2]
accion = sys.argv[1]
filas = []

if accion == "s":
        print("buscar: ", nombre, " en la web")
elif accion == "r":
        print("leer: ", nombre, "en disco")
        filas = textfile.leelineas(nombre)
        for fila in filas:
                print(fila)
elif accion == "b":
        texto = textfile.leefichero(nombre)
        textotratado = cadena.extrae("e",texto)
        for linea in textotratado:
                print(linea)
else:
        print("Accion no definida")

