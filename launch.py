import sys


nombre = sys.argv[2]
accion = sys.argv[1]

if accion == "w":
        print("buscar: ", nombre, " en la web")
else:
        print("Accion no definida")

